import { Stack, Title, Divider, ThemeIcon, Text } from "@mantine/core";

import { TField } from "@renderer/types";

import { getColor, getIcon, getText } from "./utils";

type TProps = {
  field: TField;
};

export default function FieldMonitor({ field }: TProps): React.JSX.Element {
  return (
    <Stack flex={1} align="center" justify="center">
      <Title order={2}>{field}</Title>
      <Divider w={"100%"} size={"lg"} />
      <ThemeIcon color={getColor(field)} variant="light" radius="md" size={128}>
        {getIcon(field)}
      </ThemeIcon>
      <Divider w={"100%"} size={"lg"} />
      <Text size="m">{getText(field)}</Text>
    </Stack>
  );
}
