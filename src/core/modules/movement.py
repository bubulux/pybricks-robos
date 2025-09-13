from pybricks.pupdevices import Motor
from ..utils import speedConverter


class Movement:

    def __init__(self, rightMotor: Motor, leftMotor: Motor):
        self.rightMotor = rightMotor
        self.leftMotor = leftMotor

    def forward(self, speed: int):
        convertedSpeed = speedConverter(speed)
        self.rightMotor.run(convertedSpeed)
        self.leftMotor.run(convertedSpeed)
