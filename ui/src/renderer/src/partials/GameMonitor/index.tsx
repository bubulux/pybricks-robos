import { Stack, Divider, Group, Text, Tooltip, Flex } from "@mantine/core";
import { PieChart } from "@mantine/charts";

import { IconRobot } from "@tabler/icons-react";

import { TGameStatus, TState } from "@renderer/types";

import {
  convertLeftTimeSToMMSS,
  getStateColor,
  getStateIcon,
  getStatusColor,
} from "./utils";

type TProps = {
  totalTimeS: number;
  timeLeftS: number;
  status: TGameStatus;
  state: TState;
};

export default function GameMonitor({
  totalTimeS,
  timeLeftS,
  status,
  state,
}: TProps): React.JSX.Element {
  const data = [
    { value: timeLeftS, color: "green.5", name: "Time Left" },
    {
      value: totalTimeS - timeLeftS,
      color: "red.5",
      name: "Elapsed Time",
    },
  ];

  return (
    <Stack flex={1} align="center" justify="center" gap={24}>
      <Group align="center" justify="center">
        <IconRobot size={52} />
        <Tooltip label={state} withArrow position="bottom">
          <Flex
            p={6}
            bdrs={"100px"}
            h={"fit-content"}
            w={"fit-content"}
            bg={getStateColor(state)}
          >
            {getStateIcon(state)}
          </Flex>
        </Tooltip>
      </Group>
      <Divider size="lg" w={"100%"} />
      <Group gap="xs">
        <Text fw={700} size="xl">
          Status:
        </Text>
        <Text fw={700} size="xl" c={getStatusColor(status)}>
          {status}
        </Text>
      </Group>
      <Divider size="lg" w={"100%"} />
      <PieChart data={data} strokeWidth={0} w={"100%"} />
      <Divider size="lg" w={"100%"} />
      <Group gap="xs">
        <Text size="xl" fw={700}>
          Time left:
        </Text>
        <Text size="xl" fw={700} c="blue">
          {convertLeftTimeSToMMSS(timeLeftS)}
        </Text>
      </Group>
    </Stack>
  );
}
