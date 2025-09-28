import { GameMonitorPartial } from "@renderer/partials";
import { TRobotSensorData } from "@renderer/stream/models";
import {
  selectCurrentState,
  selectMostRecentSensorData,
} from "@renderer/utils";

import { TGameStatus } from "@renderer/types";

type TProps = {
  data: TRobotSensorData;
};

export default function GameMonitor({ data }: TProps): React.JSX.Element {
  const state = selectCurrentState(data);
  const { Health, Light } = selectMostRecentSensorData(data);

  function determineGameStatus(): TGameStatus {
    if (Light === "WIN") return "Won";

    if (state === "Disconnected" || state === "Connecting") return "Idle";

    if (typeof Health === "number") {
      if (Health > 0) return "Running";
      if (Health <= 0) return "Lost";
    }

    return "Idle";
  }

  return (
    <GameMonitorPartial
      status={determineGameStatus()}
      totalTimeS={300}
      timeLeftS={290}
      state={state}
    />
  );
}
