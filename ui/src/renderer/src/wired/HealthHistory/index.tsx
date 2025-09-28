import { HealthHistoryPartial } from "@renderer/partials";
import { selectCurrenState, selectHealthHistory } from "@renderer/utils";

import { TRobotSensorData } from "@renderer/stream/models";

type TProps = {
  data: TRobotSensorData;
};

export default function HealthHistory({ data }: TProps): React.JSX.Element {
  const history = selectHealthHistory(data).map((v, i) => {
    return { time: i.toString(), value: v };
  });

  const state = selectCurrenState(data);

  return (
    <HealthHistoryPartial data={history} isLoading={state === "Connecting"} />
  );
}
