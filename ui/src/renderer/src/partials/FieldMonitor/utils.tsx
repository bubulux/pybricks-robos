import {
  IconForbid2Filled,
  IconShieldFilled,
  IconHeartPlus,
  IconHeartMinus,
  IconNut,
  IconGift,
} from "@tabler/icons-react";

import { TField } from "@renderer/types";

export function getColor(field: TField): string {
  switch (field) {
    case "Won":
      return "blue";
    case "Forbidden":
      return "red";
    case "Protected":
      return "yellow";
    case "Damaging":
      return "red";
    case "Healing":
      return "green";
    case "Protected-Damaging":
      return "grape";
    default:
      return "gray";
  }
}

export function getIcon(field: TField): React.JSX.Element {
  switch (field) {
    case "Won":
      return <IconGift size={128} />;
    case "Forbidden":
      return <IconForbid2Filled size={128} />;
    case "Protected":
      return <IconShieldFilled size={128} />;
    case "Damaging":
      return <IconHeartMinus size={128} />;
    case "Healing":
      return <IconHeartPlus size={128} />;
    case "Protected-Damaging":
      return <IconShieldFilled size={128} />;
    default:
      return <IconNut size={128} />;
  }
}

export function getText(field: TField): string {
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
    case "Won":
      return "You have reached the goal area! Congratulations!";
    case "Protected-Damaging":
      return "You are protected, but you still lose 5 health points every second!";
    default:
      return "This area has no special properties.";
  }
}
