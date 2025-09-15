import { useState, useEffect, useCallback } from "react";
import { z } from "zod";

// Zod schema for robot sensor data validation

const Literals = z.union([
  z.literal("NONE"),
  z.literal("INIT"),
  z.literal("START"),
]);

const SensorValueSchema = z.union([Literals, z.number()]);

const RobotSensorDataSchema = z.object({
  HEALTH: z.array(SensorValueSchema),
  LIGHT: z.array(z.union([Literals, z.literal("RED"), z.literal("GREEN")])),
  PRESSURE_LEFT: z.array(SensorValueSchema),
  PRESSURE_RIGHT: z.array(SensorValueSchema),
  PRESSURE_BACK: z.array(SensorValueSchema),
});

// TypeScript types derived from Zod schemas
export type SensorValue = z.infer<typeof SensorValueSchema>;
export type RobotSensorData = z.infer<typeof RobotSensorDataSchema>;

// Hook return type
export interface UseRobotDataStreamReturn {
  data: RobotSensorData;
  isLoading: boolean;
  error: string | null;
  isConnected: boolean;
}

// Validation helper
const validateRobotData = (rawData: unknown): RobotSensorData => {
  return RobotSensorDataSchema.parse(rawData);
};

/**
 * Custom hook for managing robot sensor data stream
 * Provides real-time CSV data with proper type validation
 */
export const useRobotDataStream = (): UseRobotDataStreamReturn => {
  const [data, setData] = useState<RobotSensorData>({
    HEALTH: [],
    LIGHT: [],
    PRESSURE_LEFT: [],
    PRESSURE_RIGHT: [],
    PRESSURE_BACK: [],
  });
  const [isLoading, setIsLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const [isConnected, setIsConnected] = useState(false);

  // Handle data updates with validation
  const handleDataUpdate = useCallback((rawData: unknown) => {
    try {
      const validatedData = validateRobotData(rawData);
      setData(validatedData);
      setError(null);
      setIsConnected(true);
    } catch (validationError) {
      const errorMessage =
        validationError instanceof Error
          ? validationError.message
          : "Data validation failed";
      setError(errorMessage);
      console.error("Robot data validation error:", validationError);
    }
  }, []);

  useEffect(() => {
    let unsubscribe: (() => void) | null = null;

    // eslint-disable-next-line @typescript-eslint/explicit-function-return-type
    const initializeDataStream = async () => {
      try {
        setIsLoading(true);
        setError(null);

        // Load initial CSV data
        const initialData = await window.api.getCsvData();
        handleDataUpdate(initialData);

        // Start watching for file changes
        await window.api.startWatchingCsv();

        // Subscribe to real-time updates
        unsubscribe = window.api.onCsvDataChanged((newData) => {
          handleDataUpdate(newData);
        });

        setIsConnected(true);
      } catch (err) {
        const errorMessage =
          err instanceof Error
            ? err.message
            : "Failed to initialize data stream";
        setError(errorMessage);
        setIsConnected(false);
        console.error("Failed to initialize robot data stream:", err);
      } finally {
        setIsLoading(false);
      }
    };

    initializeDataStream();

    // Cleanup function
    return () => {
      if (unsubscribe) {
        unsubscribe();
      }
      window.api.stopWatchingCsv().catch((err) => {
        console.error("Failed to stop watching CSV:", err);
      });
    };
  }, [handleDataUpdate]);

  return {
    data,
    isLoading,
    error,
    isConnected,
  };
};

export default useRobotDataStream;
