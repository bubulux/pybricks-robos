import {
  TRobotSensorData,
  TLightValue,
  TSensorValue,
} from "@renderer/stream/models";

import { TState } from "@renderer/types";

export function selectMostRecentSensorData(data: TRobotSensorData): {
  Health: Omit<TSensorValue, "NONE">;
  Light: Omit<TLightValue, "NONE">;
} {
  const healthData = data.HEALTH.filter((v) => v !== "NONE").slice(-1)[0];
  const lightData = data.LIGHT.filter((v) => v !== "NONE").slice(-1)[0];

  return {
    Health: healthData,
    Light: lightData,
  };
}

export function selectHealthHistory(data: TRobotSensorData): number[] {
  return data.HEALTH.filter((v) => typeof v === "number");
}

export function selectCurrenState(data: TRobotSensorData): TState {
  const { Health, Light } = selectMostRecentSensorData(data);

  if (Health === "INIT" || Light === "INIT") {
    return "Connecting";
  }

  if (Health === "START" || Light === "START" || typeof Health === "number") {
    return "Connected";
  }

  return "Disconnected";
}
