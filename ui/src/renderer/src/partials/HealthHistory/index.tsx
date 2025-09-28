import { Loader, Group, Title } from "@mantine/core";
import { AreaChart } from "@mantine/charts";

type TData = {
  time: string;
  value: number;
};

type TProps = {
  data: TData[];
  isLoading: boolean;
};

export default function HealthHistory({
  data,
  isLoading,
}: TProps): React.JSX.Element {
  return isLoading ? (
    <Group justify="center" align="center" flex={1} gap={10}>
      <Loader color="yellow" />
      <Title order={4}>
        Connecting to Terry, history will be available soon...
      </Title>
    </Group>
  ) : (
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
