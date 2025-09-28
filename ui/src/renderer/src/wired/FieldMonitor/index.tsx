import { FieldMonitorPartial } from "@renderer/partials";
import { TRobotSensorData } from "@renderer/stream/models";

type TProps = {
  data: TRobotSensorData;
};

export default function FieldMonitor({ data }: TProps): React.JSX.Element {
  // Here you would transform data as needed
  return <FieldMonitorPartial field="Damaging" />;
}
