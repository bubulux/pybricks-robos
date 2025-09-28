import { Stack, Title, Divider, Group, Text } from "@mantine/core";
import { PieChart } from "@mantine/charts";

import { TGameStatus } from "@renderer/types";

type TProps = {
  totalTimeS: number;
  timeLeftS: number;
  status: TGameStatus;
};

export default function GameMonitor({
  totalTimeS,
  timeLeftS,
  status,
}: TProps): React.JSX.Element {
  const data = [
    { value: timeLeftS, color: "green.5", name: "Time Left" },
    {
      value: totalTimeS - timeLeftS,
      color: "red.5",
      name: "Elapsed Time",
    },
  ];

  function convertLeftTimeSToMMSS(timeLeftS: number): string {
    const minutes = Math.floor(timeLeftS / 60);
    const seconds = timeLeftS % 60;
    return `${minutes.toString().padStart(2, "0")}:${seconds
      .toString()
      .padStart(2, "0")}`;
  }

  // Function to determine status color
  function getStatusColor(status: TGameStatus): string {
    switch (status) {
      case "Running":
        return "green";
      case "Won":
        return "blue";
      case "Lost":
        return "red";
      case "Idle":
        return "yellow";
      default:
        return "gray";
    }
  }

  return (
    <Stack p={10} flex={1} align="center" gap={24}>
      <Group gap="xs">
        <Text fw={700} size="xl">
          Status:
        </Text>
        <Text fw={700} size="xl" c={getStatusColor(status)}>
          {status}
        </Text>
      </Group>
      <Divider size="lg" w={"100%"} color="blue" bdrs="lg" />
      <PieChart data={data} strokeWidth={0} w={"100%"} />
      <Divider size="lg" w={"100%"} color="blue" bdrs="lg" />
      <Text size="xl" fw={700}>
        {convertLeftTimeSToMMSS(timeLeftS)}
      </Text>
    </Stack>
  );
}
