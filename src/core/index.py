from pybricks.hubs import PrimeHub
from pybricks.pupdevices import ColorSensor, ForceSensor, Motor

from core.modules.display import Display
from core.modules.movement.index import Movement
from core.modules.health import Health


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

        self.health = Health()
        self.movement = Movement(self.rightMotor, self.leftMotor)
        self.display = Display()
