# PyBricks-compatible streamer module
from typing import Union, Literal


class SensorStreamer:
    @staticmethod
    def printSensors(
        health: Union[int, Literal["NONE", "START", "END"]] = "NONE",
        lightState: Literal[
            "NONE",
            "START",
            "WIN",
            "FORBIDDEN",
            "HEALING",
            "PROTECTED",
            "DAMAGING",
            "NEUTRAL",
            "END",
        ] = "NONE",
        pressureLeft: Union[int, Literal["NONE", "START", "END"]] = "NONE",
        pressureRight: Union[int, Literal["NONE", "START", "END"]] = "NONE",
        pressureBack: Union[int, Literal["NONE", "START", "END"]] = "NONE",
    ) -> None:
        """
        Print sensor data in CSV format for streaming to UI

        Args:
            health: Health value (number) or "NONE"
            light: Light color ("NONE", "RED", "GREEN") or LightColor constant
            pressureLeft: Left pressure sensor value (number) or "NONE"
            pressureRight: Right pressure sensor value (number) or "NONE"
            pressureBack: Back pressure sensor value (number) or "NONE"

        Example:
            SensorStreamer.printSensors(health=100)
            SensorStreamer.printSensors(health=85, light=LightColor.GREEN)
            SensorStreamer.printSensors(pressureLeft=25, pressureRight=30)
        """
        # Convert all values to strings
        healthStr = str(health)
        lightStr = str(lightState)
        pressure_leftStr = str(pressureLeft)
        pressure_rightStr = str(pressureRight)
        pressure_backStr = str(pressureBack)

        # Print in CSV format (matches the expected schema)
        csv_line = "{},{},{},{},{}".format(
            healthStr,
            lightStr,
            pressure_leftStr,
            pressure_rightStr,
            pressure_backStr,
        )
        print(csv_line)


# Convenience functions for common use cases
def streamHealth(value: int) -> None:
    """Stream only health data"""
    SensorStreamer.printSensors(health=value)


def streamLightState(
    state: Literal["FORBIDDEN", "HEALING", "PROTECTED", "DAMAGING", "NEUTRAL", "WIN"],
) -> None:
    """Stream only light data"""
    SensorStreamer.printSensors(lightState=state)


def streamPressureLeft(value: int) -> None:
    """Stream only left pressure data"""
    SensorStreamer.printSensors(pressureLeft=value)


def streamPressureRight(value: int) -> None:
    """Stream only right pressure data"""
    SensorStreamer.printSensors(pressureRight=value)


def streamPressureBack(value: int) -> None:
    """Stream only back pressure data"""
    SensorStreamer.printSensors(pressureBack=value)


def streamStart() -> None:
    """Stream START signal for all columns"""
    SensorStreamer.printSensors(
        health="START",
        lightState="START",
        pressureLeft="START",
        pressureRight="START",
        pressureBack="START",
    )
    streamHealth(100)  # Initial health value


def streamEnd() -> None:
    """Stream END signal for all columns"""
    SensorStreamer.printSensors(
        health="END",
        lightState="END",
        pressureLeft="END",
        pressureRight="END",
        pressureBack="END",
    )
