import { TRobotSensorData } from "@renderer/stream/models";
import { DataHistoryPartial } from "@renderer/partials";
import { selectCurrentState } from "@renderer/utils";

type TProps = {
  history: boolean[];
  data: TRobotSensorData;
  resetHistory: () => void;
};

export default function DataHistory({
  history,
  data,
  resetHistory,
}: TProps): React.JSX.Element {
  const state = selectCurrentState(data);

  return (
    <DataHistoryPartial
      history={history}
      isLoading={state === "Connecting"}
      resetHistory={resetHistory}
    />
  );
}
