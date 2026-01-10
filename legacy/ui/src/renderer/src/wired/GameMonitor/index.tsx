import { useEffect, useCallback, useRef } from "react";

import { GameMonitorPartial } from "@renderer/partials";
import { TRobotSensorData } from "@renderer/stream/models";
import {
  selectCurrentState,
  selectMostRecentSensorData,
} from "@renderer/utils";

import { TGameStatus } from "@renderer/types";
import { useGameTimer } from "@renderer/wired/GameMonitor/timer";

type TProps = {
  data: TRobotSensorData;
};

export default function GameMonitor({ data }: TProps): React.JSX.Element {
  const state = selectCurrentState(data);
  const prevState = useRef(state);
  const { Health, Light } = selectMostRecentSensorData(data);
  const { totalTimeS, timeLeftS, pauseTime, restartTime } = useGameTimer();

  const isWin = useCallback((): boolean => {
    return Light === "WIN";
  }, [Light]);

  const isLose = useCallback((): boolean => {
    return typeof Health === "number" && Health <= 0;
  }, [Health]);

  function isRunning(): boolean {
    return typeof Health === "number" && Health > 0;
  }

  function determineGameStatus(): TGameStatus {
    if (timeLeftS === 0) return "Lost";

    if (isWin()) return "Won";

    if (state === "Disconnected" || state === "Connecting") return "Idle";

    if (isLose()) return "Lost";

    if (isRunning()) return "Running";

    return "Idle";
  }

  useEffect(() => {
    if (state === "Connected" && prevState.current !== "Connected")
      restartTime();
    if (state === "Disconnected" || isWin() || isLose()) {
      pauseTime();
    }
    prevState.current = state;
  }, [pauseTime, restartTime, isWin, isLose, state, Light]);

  return (
    <GameMonitorPartial
      status={determineGameStatus()}
      totalTimeS={totalTimeS}
      timeLeftS={timeLeftS}
      state={state}
    />
  );
}
