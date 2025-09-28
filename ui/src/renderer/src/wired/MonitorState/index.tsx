import { TRobotSensorData } from "@renderer/stream/models";
import { MonitorStatePartial } from "@renderer/partials";

import { selectMostRecentSensorData } from "@renderer/utils";

type TProps = {
  data: TRobotSensorData;
};

export default function MonitorState({ data }: TProps): React.JSX.Element {
  const { Health, Light } = selectMostRecentSensorData(data);

  if (Health === "INIT" || Light === "INIT") {
    return <MonitorStatePartial state="Connecting" />;
  }

  if (Health === "START" || Light === "START" || typeof Health === "number") {
    return <MonitorStatePartial state="Connected" />;
  }

  return <MonitorStatePartial state="Disconnected" />;
}
