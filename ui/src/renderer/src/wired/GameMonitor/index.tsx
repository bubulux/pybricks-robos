import { GameMonitorPartial } from "@renderer/partials";
import { TRobotSensorData } from "@renderer/stream/models";
import { selectCurrentState } from "@renderer/utils";

type TProps = {
  data: TRobotSensorData;
};

export default function GameMonitor({ data }: TProps): React.JSX.Element {
  const state = selectCurrentState(data);

  return (
    <GameMonitorPartial
      status="Idle"
      totalTimeS={300}
      timeLeftS={290}
      state={state}
    />
  );
}
