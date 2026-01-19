from typing import Literal

from pybricks.pupdevices import Motor
from .utils import convertPercentToDegreesPerSecond


class Actions:

    def __init__(self, rightMotor: Motor, leftMotor: Motor):
        self._rightMotor = rightMotor
        self._leftMotor = leftMotor

    def _controledMotor(
        self, percent: int, direction: Literal["forward", "backward"], motor: Motor
    ):
        convertedSpeed = convertPercentToDegreesPerSecond(percent)
        if direction == "forward":
            motor.run(convertedSpeed)
        else:
            motor.run(-convertedSpeed)

    def _tiltedDirection(
        self,
        dirPercent: int,
        tiltPercent: int,
        direction: Literal["forward", "backward"],
        tilt: Literal["left", "right"],
    ):
        # Determine motor speeds based on tilt direction
        if tilt == "left":
            leftPercent = min(dirPercent, tiltPercent)
            rightPercent = max(dirPercent, tiltPercent)
        else:  # tilt == "right"
            leftPercent = max(dirPercent, tiltPercent)
            rightPercent = min(dirPercent, tiltPercent)

        # Apply the speeds to the motors
        self._controledMotor(leftPercent, direction, self._leftMotor)
        self._controledMotor(rightPercent, direction, self._rightMotor)

    def stop(self):
        self._rightMotor.stop()
        self._leftMotor.stop()

    def forward(self, percent: int):
        self._controledMotor(percent, "forward", self._rightMotor)
        self._controledMotor(percent, "forward", self._leftMotor)

    def backward(self, percent: int):
        self._controledMotor(percent, "backward", self._rightMotor)
        self._controledMotor(percent, "backward", self._leftMotor)

    def turnLeft(self, percent: int):
        self._controledMotor(percent, "forward", self._rightMotor)
        self._controledMotor(percent, "backward", self._leftMotor)

    def turnRight(self, percent: int):
        self._controledMotor(percent, "backward", self._rightMotor)
        self._controledMotor(percent, "forward", self._leftMotor)

    def forwardLeft(self, dirPercent: int, tiltPercent: int):
        self._tiltedDirection(dirPercent, tiltPercent, "forward", "left")

    def forwardRight(self, dirPercent: int, tiltPercent: int):
        self._tiltedDirection(dirPercent, tiltPercent, "forward", "right")

    def backwardLeft(self, dirPercent: int, tiltPercent: int):
        self._tiltedDirection(dirPercent, tiltPercent, "backward", "left")

    def backwardRight(self, dirPercent: int, tiltPercent: int):
        self._tiltedDirection(dirPercent, tiltPercent, "backward", "right")
