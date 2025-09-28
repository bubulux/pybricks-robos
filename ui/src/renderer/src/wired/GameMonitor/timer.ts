import { useState, useEffect, useRef, useCallback } from "react";

interface UseGameTimerProps {
  initialTimeS?: number;
  autoStart?: boolean;
}

interface UseGameTimerReturn {
  totalTimeS: number;
  timeLeftS: number;
  pauseTime: () => void;
  restartTime: () => void;
  isRunning: boolean;
  startTime: () => void;
}

/**
 * A custom React hook that provides timing functionality for the game monitor.
 *
 * @param initialTimeS - Initial total time in seconds (default: 300 seconds / 5 minutes)
 * @param autoStart - Whether to automatically start the timer when mounted (default: false)
 * @returns An object with timing control functions and current time values
 */
export const useGameTimer = ({
  initialTimeS = 60,
  autoStart = false,
}: UseGameTimerProps = {}): UseGameTimerReturn => {
  const [totalTimeS] = useState<number>(initialTimeS);
  const [timeLeftS, setTimeLeftS] = useState<number>(initialTimeS);
  const [isRunning, setIsRunning] = useState<boolean>(autoStart);

  // Using a ref to track the interval ID
  const intervalRef = useRef<number | null>(null);

  // Clean up the interval when component unmounts
  useEffect(() => {
    return () => {
      if (intervalRef.current !== null) {
        window.clearInterval(intervalRef.current);
      }
    };
  }, []);

  // Effect to handle the timer counting down
  useEffect(() => {
    if (isRunning) {
      intervalRef.current = window.setInterval(() => {
        setTimeLeftS((prevTime) => {
          const newTime = prevTime - 1;
          // Stop the timer when it reaches 0
          if (newTime <= 0) {
            if (intervalRef.current !== null) {
              window.clearInterval(intervalRef.current);
              setIsRunning(false);
            }
            return 0;
          }
          return newTime;
        });
      }, 1000);
    } else if (intervalRef.current !== null) {
      window.clearInterval(intervalRef.current);
      intervalRef.current = null;
    }

    return () => {
      if (intervalRef.current !== null) {
        window.clearInterval(intervalRef.current);
      }
    };
  }, [isRunning]);

  /**
   * Pause the timer
   */
  const pauseTime = useCallback(() => {
    setIsRunning(false);
  }, []);

  /**
   * Start the timer
   */
  const startTime = useCallback(() => {
    setIsRunning(true);
  }, []);

  /**
   * Restart the timer back to the initial time
   */
  const restartTime = useCallback(() => {
    setTimeLeftS(totalTimeS);
    setIsRunning(true);
  }, [totalTimeS]);

  return {
    totalTimeS,
    timeLeftS,
    pauseTime,
    restartTime,
    isRunning,
    startTime,
  };
};
