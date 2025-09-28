export type TState = "Connected" | "Disconnected" | "Connecting";

export type TGameStatus = "Running" | "Won" | "Lost" | "Idle";

export type TField =
  | "Forbidden"
  | "Healing"
  | "Protected"
  | "Neutral"
  | "Damaging"
  | "Won";
