import { ElectronAPI } from "@electron-toolkit/preload";

interface LogAPI {
  getLogContent: () => Promise<string>;
  startWatchingLog: () => Promise<void>;
  stopWatchingLog: () => Promise<void>;
  onLogFileChanged: (callback: (content: string) => void) => () => void;
}

declare global {
  interface Window {
    electron: ElectronAPI;
    api: LogAPI;
  }
}
