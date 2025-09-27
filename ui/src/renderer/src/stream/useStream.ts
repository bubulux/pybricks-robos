import { useState, useEffect, useCallback } from "react";

import { TRobotSensorData, ZRobotSensorData } from "./models";

export default function useStream(): {
  data: TRobotSensorData;
  history: boolean[];
} {
  const [data, setData] = useState<TRobotSensorData>({
    HEALTH: [],
    LIGHT: [],
    PRESSURE_LEFT: [],
    PRESSURE_RIGHT: [],
    PRESSURE_BACK: [],
  });

  const [history, setHistory] = useState<boolean[]>([]);

  const handleNewData = useCallback((rawData: unknown) => {
    const parsed = ZRobotSensorData.safeParse(rawData);
    if (parsed.success) {
      setData(parsed.data);
      setHistory((prev) => [...prev, true]);
    } else {
      setHistory((prev) => [...prev, false]);
    }
  }, []);

  useEffect(() => {
    let unsubscribe: (() => void) | null = null;

    async function initialize(): Promise<void> {
      const initialData = await window.api.getCsvData();
      handleNewData(initialData);

      await window.api.startWatchingCsv();

      unsubscribe = window.api.onCsvDataChanged((newData) => {
        handleNewData(newData);
      });
    }

    initialize();

    return () => {
      if (unsubscribe) {
        unsubscribe();
      }
      window.api.stopWatchingCsv();
    };
  }, [handleNewData]);

  return { data, history };
}
