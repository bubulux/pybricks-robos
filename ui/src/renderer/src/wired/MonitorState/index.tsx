import { TRobotSensorData } from "@renderer/stream/models";
import { MonitorStatePartial } from "@renderer/partials";

import { selectCurrenState } from "@renderer/utils";

type TProps = {
  data: TRobotSensorData;
};

export default function MonitorState({ data }: TProps): React.JSX.Element {
  const state = selectCurrenState(data);
  return <MonitorStatePartial state={state} />;
}
