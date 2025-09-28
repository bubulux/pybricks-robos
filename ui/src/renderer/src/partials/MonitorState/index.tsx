import { Loader, Title, Stack, Flex, Group, Tooltip, Box } from "@mantine/core";

import {
  IconAlertCircle,
  IconCircleCheck,
  IconRobot,
} from "@tabler/icons-react";

import { TState } from "@renderer/types";

type TProps = {
  state: TState;
};

export default function MonitorState({ state }: TProps): React.JSX.Element {
  return (
    <Stack align="center" justify="center" flex={1}>
      <Title order={4}>
        <Group gap={4}>
          Terry
          <IconRobot size={20} />
        </Group>
      </Title>
      <Tooltip label={state} withArrow position="bottom">
        <Flex
          p={6}
          bdrs={"100px"}
          h={"fit-content"}
          w={"fit-content"}
          bg={
            state === "Disconnected"
              ? "red"
              : state === "Connecting"
                ? "yellow"
                : "green"
          }
        >
          {state === "Disconnected" ? (
            <IconAlertCircle size={48} color="white" />
          ) : state === "Connecting" ? (
            <Loader color="white" size="lg" />
          ) : (
            <IconCircleCheck size={48} color="white" />
          )}
        </Flex>
      </Tooltip>
    </Stack>
  );
}
