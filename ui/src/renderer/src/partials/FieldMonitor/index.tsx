import { Stack, Title, Divider, ThemeIcon, Text } from "@mantine/core";

import {
  IconForbid2Filled,
  IconShieldFilled,
  IconHeartPlus,
  IconHeartMinus,
  IconNut,
} from "@tabler/icons-react";

import { TField } from "@renderer/types";

type TProps = {
  field: TField;
};

export default function FieldMonitor({ field }: TProps): React.JSX.Element {
  function getColor(field: TField): string {
    switch (field) {
      case "Forbidden":
        return "red";
      case "Protected":
        return "blue";
      case "Damaging":
        return "red";
      case "Healing":
        return "green";
      case "Neutral":
        return "gray";
      default:
        return "gray";
    }
  }

  function getIcon(field: TField): React.JSX.Element {
    switch (field) {
      case "Forbidden":
        return <IconForbid2Filled size={128} />;
      case "Protected":
        return <IconShieldFilled size={128} />;
      case "Damaging":
        return <IconHeartMinus size={128} />;
      case "Healing":
        return <IconHeartPlus size={128} />;
      case "Neutral":
        return <IconNut size={128} />;
      default:
        return <IconNut size={128} />;
    }
  }

  function getText(field: TField): string {
    switch (field) {
      case "Forbidden":
        return "Every second on this area costs 20 health points!";
      case "Protected":
        return "You cannot be damaged on this area!";
      case "Damaging":
        return "Every second on this area reduces 3 health points!";
      case "Healing":
        return "Every second on this area restores 5 health points!";
      case "Neutral":
        return "This area has no special properties.";
      default:
        return "This area has no special properties.";
    }
  }

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
