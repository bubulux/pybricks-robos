import { TGameStatus, TState } from "@renderer/types";

import { Loader } from "@mantine/core";
import { IconAlertCircle, IconCircleCheck } from "@tabler/icons-react";

export function convertLeftTimeSToMMSS(timeLeftS: number): string {
  const minutes = Math.floor(timeLeftS / 60);
  const seconds = timeLeftS % 60;
  return `${minutes.toString().padStart(2, "0")}:${seconds
    .toString()
    .padStart(2, "0")}`;
}

export function getStatusColor(status: TGameStatus): string {
  switch (status) {
    case "Running":
      return "green";
    case "Won":
      return "blue";
    case "Lost":
      return "red";
    case "Idle":
      return "yellow";
    default:
      return "gray";
  }
}

export function getStateColor(state: TState): string {
  switch (state) {
    case "Connected":
      return "green";
    case "Connecting":
      return "yellow";
    case "Disconnected":
      return "red";
    default:
      return "gray";
  }
}

export function getStateIcon(state: TState): React.JSX.Element {
  switch (state) {
    case "Connected":
      return <IconCircleCheck size={48} color="white" />;
    case "Connecting":
      return <Loader color="white" size="lg" />;
    case "Disconnected":
      return <IconAlertCircle size={48} color="white" />;
    default:
      return <IconAlertCircle size={48} color="white" />;
  }
}
