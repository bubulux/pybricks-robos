import { Group, Box } from "@mantine/core";

type TProps = {
  history: boolean[];
};

export default function DataHistory({ history }: TProps): React.JSX.Element {
  return (
    <Group gap={0} flex={1} justify="space-evenly">
      {history.map((state, index) => (
        <Box key={index} bg={state ? "green" : "red"} h={"100%"} flex={1} />
      ))}
    </Group>
  );
}
