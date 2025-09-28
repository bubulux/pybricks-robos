import { AreaChart } from "@mantine/charts";

type TData = {
  time: string;
  value: number;
};

type TProps = {
  data: TData[];
};

export default function HealthHistory({ data }: TProps): React.JSX.Element {
  return (
    <AreaChart
      withXAxis={false}
      withYAxis={false}
      style={{
        padding: 10,
      }}
      data={data}
      dataKey="time"
      series={[{ name: "value", color: "green" }]}
    />
  );
}
