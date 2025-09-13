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
        withDirection = convertedSpeed if direction == "forward" else -convertedSpeed
        motor.run(withDirection)

    def stop(self):
        self._rightMotor.stop()
        self._leftMotor.stop()

    def forward(self, percent: int):
        self._controledMotor(percent, "forward", self._rightMotor)
        self._controledMotor(percent, "forward", self._leftMotor)

    def backward(self, percent: int):
        self._controledMotor(percent, "backward", self._rightMotor)
        self._controledMotor(percent, "backward", self._leftMotor)
