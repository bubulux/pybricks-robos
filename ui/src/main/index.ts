import { app, shell, BrowserWindow, ipcMain } from "electron";
import { join } from "path";
import { electronApp, optimizer, is } from "@electron-toolkit/utils";
import icon from "../../resources/icon.png?asset";
import { readFileSync } from "fs";
import * as chokidar from "chokidar";
import installExtension, {
  REACT_DEVELOPER_TOOLS,
} from "electron-devtools-installer";

function createWindow(): void {
  // Create the browser window.
  const mainWindow = new BrowserWindow({
    width: 900,
    height: 670,
    show: false,
    autoHideMenuBar: true,
    ...(process.platform === "linux" ? { icon } : {}),
    webPreferences: {
      preload: join(__dirname, "../preload/index.js"),
      sandbox: false,
    },
  });

  mainWindow.on("ready-to-show", () => {
    mainWindow.show();
  });

  mainWindow.webContents.setWindowOpenHandler((details) => {
    shell.openExternal(details.url);
    return { action: "deny" };
  });

  // HMR for renderer base on electron-vite cli.
  // Load the remote URL for development or the local html file for production.
  if (is.dev && process.env["ELECTRON_RENDERER_URL"]) {
    mainWindow.loadURL(process.env["ELECTRON_RENDERER_URL"]);
  } else {
    mainWindow.loadFile(join(__dirname, "../renderer/index.html"));
  }
}

// This method will be called when Electron has finished
// initialization and is ready to create browser windows.
// Some APIs can only be used after this event occurs.
app.whenReady().then(async () => {
  // Install React DevTools
  if (is.dev) {
    try {
      await installExtension(REACT_DEVELOPER_TOOLS);
      console.log("React DevTools installed successfully");
    } catch (err) {
      console.log("Error installing React DevTools: ", err);
    }
  }

  // Set app user model id for windows
  electronApp.setAppUserModelId("com.electron");

  // Default open or close DevTools by F12 in development
  // and ignore CommandOrControl + R in production.
  // see https://github.com/alex8088/electron-toolkit/tree/master/packages/utils
  app.on("browser-window-created", (_, window) => {
    optimizer.watchWindowShortcuts(window);
  });

  // IPC test
  ipcMain.on("ping", () => console.log("pong"));

  // File watching setup
  // Watch the CSV file for sensor data
  const csvFilePath = join(__dirname, "../../stream/info.csv");

  console.log("Looking for CSV file at:", csvFilePath);

  // Function to parse CSV into history map
  function parseCSVToHistoryMap(
    csvContent: string,
  ): Record<string, (string | number)[]> {
    const lines = csvContent.trim().split("\n");
    if (lines.length < 2) {
      return {};
    }

    // Get headers from first line
    const headers = lines[0].split(",").map((h) => h.trim());
    const result: Record<string, (string | number)[]> = {};

    // Initialize arrays for each header
    headers.forEach((header) => {
      result[header] = [];
    });

    // Process data rows (skip header)
    for (let i = 1; i < lines.length; i++) {
      const values = lines[i].split(",").map((v) => v.trim());
      headers.forEach((header, index) => {
        const value = values[index] || "NONE";
        // Convert to number if it's numeric, otherwise keep as string
        const parsedValue =
          value === "NONE"
            ? "NONE"
            : !isNaN(Number(value))
              ? Number(value)
              : value;
        result[header].push(parsedValue);
      });
    }

    return result;
  }

  // Handle request for initial CSV data
  ipcMain.handle("get-csv-data", () => {
    try {
      const content = readFileSync(csvFilePath, "utf-8");
      return parseCSVToHistoryMap(content);
    } catch (error) {
      console.error("Error reading CSV file:", error);
      return {};
    }
  });

  // Watch for file changes
  let fileWatcher: chokidar.FSWatcher | null = null;
  let pollingInterval: NodeJS.Timeout | null = null;
  let lastFileContent = "";
  let debounceTimer: NodeJS.Timeout | null = null;

  ipcMain.handle("start-watching-csv", () => {
    if (fileWatcher || pollingInterval) {
      return; // Already watching
    }

    // Read initial content
    try {
      lastFileContent = readFileSync(csvFilePath, "utf-8");
    } catch (error) {
      console.error("Error reading initial CSV content:", error);
      lastFileContent = "";
    }

    try {
      // Use chokidar for file system events (fast detection)
      fileWatcher = chokidar.watch(csvFilePath, {
        persistent: true,
        usePolling: false,
        ignoreInitial: true,
        awaitWriteFinish: {
          stabilityThreshold: 50,
          pollInterval: 25,
        },
      });

      fileWatcher.on("change", () => {
        console.log("Chokidar detected file change");
        handleFileChange();
      });

      fileWatcher.on("error", (error) => {
        console.error("File watcher error:", error);
      });

      // Also use polling as a fallback for Python script locks (reliable detection)
      pollingInterval = setInterval(() => {
        try {
          const currentContent = readFileSync(csvFilePath, "utf-8");
          if (currentContent !== lastFileContent) {
            console.log("Polling detected file change");
            lastFileContent = currentContent;
            handleFileChange();
          }
        } catch {
          // File might be locked, that's ok, we'll try again
        }
      }, 100); // Poll every 100ms

      console.log(
        "Started watching CSV file with chokidar + polling:",
        csvFilePath,
      );
    } catch (error) {
      console.error("Error starting file watcher:", error);
    }
  });

  // Centralized file change handler
  function handleFileChange(): void {
    if (debounceTimer) {
      clearTimeout(debounceTimer);
    }

    debounceTimer = setTimeout(() => {
      try {
        const content = readFileSync(csvFilePath, "utf-8");
        lastFileContent = content; // Update our cache
        const parsedData = parseCSVToHistoryMap(content);
        console.log("CSV file changed, sending update to renderer");

        // Send updated data to all renderer processes
        BrowserWindow.getAllWindows().forEach((window) => {
          window.webContents.send("csv-data-changed", parsedData);
        });
      } catch (error) {
        console.error("Error reading updated CSV file:", error);
        // Retry after a short delay if the file is locked
        setTimeout(() => {
          try {
            const content = readFileSync(csvFilePath, "utf-8");
            lastFileContent = content;
            const parsedData = parseCSVToHistoryMap(content);
            BrowserWindow.getAllWindows().forEach((window) => {
              window.webContents.send("csv-data-changed", parsedData);
            });
          } catch (retryError) {
            console.error("Retry failed:", retryError);
          }
        }, 150);
      }
    }, 50); // 50ms debounce delay
  }

  ipcMain.handle("stop-watching-csv", () => {
    if (debounceTimer) {
      clearTimeout(debounceTimer);
      debounceTimer = null;
    }
    if (pollingInterval) {
      clearInterval(pollingInterval);
      pollingInterval = null;
    }
    if (fileWatcher) {
      fileWatcher.close();
      fileWatcher = null;
    }
    console.log("Stopped watching CSV file");
  });

  createWindow();

  app.on("activate", function () {
    // On macOS it's common to re-create a window in the app when the
    // dock icon is clicked and there are no other windows open.
    if (BrowserWindow.getAllWindows().length === 0) createWindow();
  });
});

// Quit when all windows are closed, except on macOS. There, it's common
// for applications and their menu bar to stay active until the user quits
// explicitly with Cmd + Q.
app.on("window-all-closed", () => {
  if (process.platform !== "darwin") {
    app.quit();
  }
});

// In this file you can include the rest of your app's specific main process
// code. You can also put them in separate files and require them here.
