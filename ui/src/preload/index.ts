import { contextBridge, ipcRenderer } from "electron";
import { electronAPI } from "@electron-toolkit/preload";

// Custom APIs for renderer
const api = {
  // Log file watching
  getLogContent: () => ipcRenderer.invoke("get-log-content"),
  startWatchingLog: () => ipcRenderer.invoke("start-watching-log"),
  stopWatchingLog: () => ipcRenderer.invoke("stop-watching-log"),
  onLogFileChanged: (callback: (content: string) => void) => {
    const unsubscribe = (
      _event: Electron.IpcRendererEvent,
      content: string,
    ): void => callback(content);
    ipcRenderer.on("log-file-changed", unsubscribe);

    // Return cleanup function
    return () => ipcRenderer.removeListener("log-file-changed", unsubscribe);
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
