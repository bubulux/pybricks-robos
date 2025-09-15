import { app, shell, BrowserWindow, ipcMain } from "electron";
import { join } from "path";
import { electronApp, optimizer, is } from "@electron-toolkit/utils";
import icon from "../../resources/icon.png?asset";
import { readFileSync, watch, type FSWatcher } from "fs";

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
app.whenReady().then(() => {
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
  // The log file is now in ui/logs/ directory
  const logFilePath = join(
    __dirname,
    "../../logs/robot_log_20250914_144928.txt",
  );

  console.log("Looking for log file at:", logFilePath);

  // Handle request for initial file content
  ipcMain.handle("get-log-content", () => {
    try {
      return readFileSync(logFilePath, "utf-8");
    } catch (error) {
      console.error("Error reading log file:", error);
      return "Error reading log file";
    }
  });

  // Watch for file changes
  let fileWatcher: FSWatcher | null = null;

  ipcMain.handle("start-watching-log", () => {
    if (fileWatcher) {
      return; // Already watching
    }

    try {
      fileWatcher = watch(logFilePath, (eventType) => {
        if (eventType === "change") {
          try {
            const content = readFileSync(logFilePath, "utf-8");
            // Send updated content to all renderer processes
            BrowserWindow.getAllWindows().forEach((window) => {
              window.webContents.send("log-file-changed", content);
            });
          } catch (error) {
            console.error("Error reading updated log file:", error);
          }
        }
      });
      console.log("Started watching log file:", logFilePath);
    } catch (error) {
      console.error("Error starting file watcher:", error);
    }
  });

  ipcMain.handle("stop-watching-log", () => {
    if (fileWatcher) {
      fileWatcher.close();
      fileWatcher = null;
      console.log("Stopped watching log file");
    }
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
