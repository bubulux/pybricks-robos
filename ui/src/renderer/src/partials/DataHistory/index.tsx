import { Group, Box } from "@mantine/core";

type TProps = {
  history: boolean[];
  isLoading: boolean;
};

export default function DataHistory({
  history,
  isLoading,
}: TProps): React.JSX.Element {
  return (
    <Group gap={0} flex={1} justify="space-evenly" bg={"yellow.1"}>
      {!isLoading &&
        history.map((state, index) => (
          <Box key={index} bg={state ? "green.3" : "red"} h={"100%"} flex={1} />
        ))}
    </Group>
  );
}
