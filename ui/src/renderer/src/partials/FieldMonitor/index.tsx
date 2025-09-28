import { Stack, Title } from "@mantine/core";

type TProps = Record<string, never>;

export default function FieldMonitor(_props: TProps): React.JSX.Element {
  return (
    <Stack>
      <Title order={4}>Field Monitor</Title>
    </Stack>
  );
}
