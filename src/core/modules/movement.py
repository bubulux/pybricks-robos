from typing import Literal

from pybricks.pupdevices import Motor
from core.utils import convertPercentToDegreesPerSecond


class Movement:

    def __init__(self, rightMotor: Motor, leftMotor: Motor):
        self._rightMotor = rightMotor
        self._leftMotor = leftMotor

    def _controledMotor(
        self, percent: int, direction: Literal["forward", "backward"], motor: Motor
    ):
        convertedSpeed = convertPercentToDegreesPerSecond(percent)
        if direction == "forward":
            print(convertedSpeed)
            motor.run(convertedSpeed)
        else:
            print(-convertedSpeed)
            motor.run(-convertedSpeed)

    def stop(self):
        print("stop")
        self._rightMotor.stop()
        self._leftMotor.stop()

    def forward(self, percent: int):
        print("forward")
        self._controledMotor(percent, "forward", self._rightMotor)
        self._controledMotor(percent, "forward", self._leftMotor)

    def backward(self, percent: int):
        print("backward")
        self._controledMotor(percent, "backward", self._rightMotor)
        self._controledMotor(percent, "backward", self._leftMotor)

    def turnLeft(self, percent: int):
        print("turnLeft")
        self._controledMotor(percent, "forward", self._rightMotor)
        self._controledMotor(percent, "backward", self._leftMotor)

    def turnRight(self, percent: int):
        print("turnRight")
        self._controledMotor(percent, "backward", self._rightMotor)
        self._controledMotor(percent, "forward", self._leftMotor)
