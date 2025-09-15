import { contextBridge, ipcRenderer } from "electron";
import { electronAPI } from "@electron-toolkit/preload";

// Custom APIs for renderer
const api = {
  // CSV file watching
  getCsvData: () => ipcRenderer.invoke("get-csv-data"),
  startWatchingCsv: () => ipcRenderer.invoke("start-watching-csv"),
  stopWatchingCsv: () => ipcRenderer.invoke("stop-watching-csv"),
  onCsvDataChanged: (
    callback: (data: Record<string, (string | number)[]>) => void,
  ) => {
    const unsubscribe = (
      _event: Electron.IpcRendererEvent,
      data: Record<string, (string | number)[]>,
    ): void => callback(data);
    ipcRenderer.on("csv-data-changed", unsubscribe);

    // Return cleanup function
    return () => ipcRenderer.removeListener("csv-data-changed", unsubscribe);
  },
};

// Use `contextBridge` APIs to expose Electron APIs to
// renderer only if context isolation is enabled, otherwise
// just add to the DOM global.
if (process.contextIsolated) {
  try {
    contextBridge.exposeInMainWorld("electron", electronAPI);
    contextBridge.exposeInMainWorld("api", api);
  } catch (error) {
    console.error(error);
  }
} else {
  // @ts-ignore (define in dts)
  window.electron = electronAPI;
  // @ts-ignore (define in dts)
  window.api = api;
}
