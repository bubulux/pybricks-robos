# PyBricks-compatible streamer module
from typing import Union, Literal


class LightColor:
    """Constants for valid light color values"""

    NONE = "NONE"
    RED = "RED"
    GREEN = "GREEN"


class SensorStreamer:
    @staticmethod
    def printSensors(
        health: Union[int, Literal["NONE", "START"]] = "NONE",
        light: Union[LightColor, Literal["NONE", "START"]] = "NONE",
        pressureLeft: Union[int, Literal["NONE", "START"]] = "NONE",
        pressureRight: Union[int, Literal["NONE", "START"]] = "NONE",
        pressureBack: Union[int, Literal["NONE", "START"]] = "NONE",
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
        lightStr = str(light)
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


def streamLight(color: LightColor) -> None:
    """Stream only light data"""
    SensorStreamer.printSensors(light=color)


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
        light="START",
        pressureLeft="START",
        pressureRight="START",
        pressureBack="START",
    )
