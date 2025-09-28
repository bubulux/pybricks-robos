import { DataHistoryPartial } from "@renderer/partials";

type TProps = {
  history: boolean[];
};

export default function DataHistory({ history }: TProps): React.JSX.Element {
  return <DataHistoryPartial history={history} />;
}
