import { DataHistoryPartial } from "@renderer/partials";

type TProps = {
  history: boolean[];
};

export default function DataHistory({ history }: TProps): React.JSX.Element {
  // Here you would transform data as needed
  return <DataHistoryPartial />;
}
