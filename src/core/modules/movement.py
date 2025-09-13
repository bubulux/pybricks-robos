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
            motor.run(convertedSpeed)
        else:
            motor.run(-convertedSpeed)

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
        # three cases
        # 1. dirPercent is smaller tiltPercent -> OKAY, the higher the offset the higher the Angle
        # 2. dirPercent is equal tiltPercent -> like Forward / Backward
        # 3. dirPercent is larger tiltPercent -> would mean inverse, so forwardRight -> needs to be inversed
        #

        leftPercent = dirPercent
        rightPercent = tiltPercent

        if dirPercent > tiltPercent:
            leftPercent = tiltPercent
            rightPercent = dirPercent

        self._controledMotor(leftPercent, "forward", self._leftMotor)
        self._controledMotor(rightPercent, "forward", self._rightMotor)
