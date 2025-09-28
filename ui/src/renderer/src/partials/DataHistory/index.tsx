import { BarChart } from "@mantine/charts";

type TProps = {
  history: {
    time: number;
    value: "Success" | "Error";
  }[];
};

export default function DataHistory({ history }: TProps): React.JSX.Element {
  return (
    <BarChart
      type="percent"
      orientation="horizontal"
      withXAxis={false}
      withYAxis={false}
    />
  );
}
