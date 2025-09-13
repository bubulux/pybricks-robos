from pybricks.hubs import PrimeHub
from pybricks.pupdevices import ColorSensor, ForceSensor, Motor


class Core:

    def __init__(
        self,
        primeHub: PrimeHub,
        rightFeel: ForceSensor,
        leftFeel: ForceSensor,
        backFeel: ForceSensor,
        colorSensor: ColorSensor,
        rightMotor: Motor,
        leftMotor: Motor,
    ):
        self.primeHub = primeHub
        self.rightFeel = rightFeel
        self.leftFeel = leftFeel
        self.backFeel = backFeel
        self.colorSensor = colorSensor
        self.rightMotor = rightMotor
        self.leftMotor = leftMotor
