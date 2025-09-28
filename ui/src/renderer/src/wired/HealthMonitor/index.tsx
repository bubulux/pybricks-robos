import { HealthMonitorPartial } from "@renderer/partials";
import { TRobotSensorData } from "@renderer/stream/models";

type TProps = {
  data: TRobotSensorData;
};

export default function HealthMonitor({ data }: TProps): React.JSX.Element {
  return (
    <HealthMonitorPartial
      health={50}
      currentEffect="neutral"
      effectImpact={10}
    />
  );
}
