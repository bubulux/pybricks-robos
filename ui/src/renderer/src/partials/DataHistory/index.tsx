import { Group, Box, ActionIcon } from "@mantine/core";
import { IconRestore } from "@tabler/icons-react";

type TProps = {
  history: boolean[];
  isLoading: boolean;
  resetHistory: () => void;
};

export default function DataHistory({
  history,
  isLoading,
  resetHistory,
}: TProps): React.JSX.Element {
  return (
    <Group flex={1}>
      <ActionIcon
        variant="outline"
        size={"s"}
        onClick={() => {
          resetHistory();
        }}
      >
        <IconRestore />
      </ActionIcon>
      <Group gap={0} flex={1} bg={"yellow.1"} h={"100%"}>
        {!isLoading &&
          history.map((state, index) => (
            <Box
              key={index}
              bg={state ? "green.3" : "red"}
              h={"100%"}
              flex={1}
            />
          ))}
      </Group>
    </Group>
  );
}
