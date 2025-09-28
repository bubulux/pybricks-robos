import { HealthMonitorPartial } from "@renderer/partials";
import { TRobotSensorData } from "@renderer/stream/models";
import {
  selectMostRecentHealthNumber,
  selectMostRecentLightEffect,
} from "@renderer/utils";

type TProps = {
  data: TRobotSensorData;
};

export default function HealthMonitor({ data }: TProps): React.JSX.Element {
  const health = selectMostRecentHealthNumber(data);
  const { mode, effect } = selectMostRecentLightEffect(data);

  return (
    <HealthMonitorPartial
      health={health}
      currentEffect={mode}
      effectImpact={effect}
    />
  );
}
