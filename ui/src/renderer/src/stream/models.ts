import z from "zod";

const ZLiterals = z.union([
  z.literal("NONE"),
  z.literal("INIT"),
  z.literal("START"),
  z.literal("END"),
]);

const ZLightLiterals = z.union([
  ZLiterals,
  z.literal("FORBIDDEN"),
  z.literal("HEALING"),
  z.literal("PROTECTED"),
  z.literal("DAMAGING"),
  z.literal("NEUTRAL"),
  z.literal("WIN"),
]);

const ZSensorValue = z.union([ZLiterals, z.number()]);

export const ZRobotSensorData = z.object({
  HEALTH: z.array(ZSensorValue),
  LIGHT: z.array(ZLightLiterals),
  PRESSURE_LEFT: z.array(ZSensorValue),
  PRESSURE_RIGHT: z.array(ZSensorValue),
  PRESSURE_BACK: z.array(ZSensorValue),
});

export type TSensorValue = z.infer<typeof ZSensorValue>;
export type TRobotSensorData = z.infer<typeof ZRobotSensorData>;
export type TLightValue = z.infer<typeof ZLightLiterals>;
