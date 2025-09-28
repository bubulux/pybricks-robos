import { Stack, Title } from "@mantine/core";

type TProps = Record<string, never>;

export default function HealthMonitor(_props: TProps): React.JSX.Element {
  return (
    <Stack>
      <Title order={4}>HealthMonitor</Title>
    </Stack>
  );
}
