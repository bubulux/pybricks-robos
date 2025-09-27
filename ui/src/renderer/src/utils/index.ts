import {
  TRobotSensorData,
  TLightValue,
  TSensorValue,
} from "@renderer/stream/models";

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
