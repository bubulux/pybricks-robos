import {
  TRobotSensorData,
  TLightValue,
  TSensorValue,
} from "@renderer/stream/models";

import { TState } from "@renderer/types";

export function selectMostRecentSensorData(data: TRobotSensorData): {
  Health: Exclude<TSensorValue, "NONE">;
  Light: Exclude<TLightValue, "NONE">;
} {
  const healthData = data.HEALTH.filter((v) => v !== "NONE").slice(-1)[0];
  const lightData = data.LIGHT.filter((v) => v !== "NONE").slice(-1)[0];

  return {
    Health: healthData,
    Light: lightData,
  };
}

export function selectMostRecentHealthNumber(data: TRobotSensorData): number {
  const healthData = data.HEALTH.filter((v) => typeof v === "number").slice(
    -1,
  )[0];
  return typeof healthData === "number" ? healthData : 0;
}

export function selectMostRecentLightEffect(data: TRobotSensorData): {
  mode: "harm" | "heal" | "neutral";
  effect: number;
} {
  const lightData = data.LIGHT.filter((v) => {
    return (
      v === "DAMAGING" ||
      v === "PROTECTED-DAMAGING" ||
      v === "FORBIDDEN" ||
      v === "NEUTRAL" ||
      v === "HEALING"
    );
  });

  const light = lightData.slice(-1)[0];

  if (light === "DAMAGING") return { mode: "harm", effect: 3 };

  if (light === "FORBIDDEN") return { mode: "harm", effect: 20 };

  if (light === "HEALING") return { mode: "heal", effect: 5 };

  if (light === "PROTECTED-DAMAGING") return { mode: "harm", effect: 5 };

  return { mode: "neutral", effect: 0 };
}

export function selectHealthHistory(data: TRobotSensorData): number[] {
  return data.HEALTH.filter((v) => typeof v === "number");
}

export function selectCurrentState(data: TRobotSensorData): TState {
  const { Health, Light } = selectMostRecentSensorData(data);

  if (Health === "INIT" || Light === "INIT") {
    return "Connecting";
  }

  if (Health === "START" || Light === "START" || typeof Health === "number") {
    return "Connected";
  }

  return "Disconnected";
}
