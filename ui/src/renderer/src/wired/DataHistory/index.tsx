import { DataHistoryPartial } from "@renderer/partials";

type TProps = {
  history: boolean[];
};

export default function DataHistory({ history }: TProps): React.JSX.Element {
  const mockData = [
    {
      time: 1,
      value: "Success",
    },
    {
      time: 2,
      value: "Error",
    },
    {
      time: 3,
      value: "Success",
    },
    {
      time: 4,
      value: "Success",
    },
    {
      time: 5,
      value: "Error",
    },
  ] as { time: number; value: "Success" | "Error" }[];

  return <DataHistoryPartial history={mockData} />;
}
