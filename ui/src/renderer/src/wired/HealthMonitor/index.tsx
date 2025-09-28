import { HealthMonitorPartial } from "@renderer/partials";
import { TRobotSensorData } from "@renderer/stream/models";

type TProps = {
  data: TRobotSensorData;
};

export default function HealthMonitor({ data }: TProps): React.JSX.Element {
  // Here you would transform data as needed
  return <HealthMonitorPartial />;
}
