import { ElectronAPI } from "@electron-toolkit/preload";

interface CsvAPI {
  getCsvData: () => Promise<Record<string, (string | number)[]>>;
  startWatchingCsv: () => Promise<void>;
  stopWatchingCsv: () => Promise<void>;
  onCsvDataChanged: (
    callback: (data: Record<string, (string | number)[]>) => void,
  ) => () => void;
}

declare global {
  interface Window {
    electron: ElectronAPI;
    api: CsvAPI;
  }
}
