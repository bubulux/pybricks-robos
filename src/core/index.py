from typing import Callable

from pybricks.hubs import PrimeHub
from pybricks.pupdevices import ColorSensor, ForceSensor, Motor

from core.modules.display import Display
from core.modules.movement.index import Movement
from core.modules.health import Health

from io.feeler import Feeler
from io.color import Color


class Core:

    def __init__(
        self,
        eventLoopRefreshRate: int,
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
        self.isProtected = False

        self.health = Health(self.isProtected)
        self.movement = Movement(self.rightMotor, self.leftMotor)
        self.display = Display()
        self.feeler = Feeler(
            self.leftFeel,
            self.rightFeel,
            self.backFeel,
            self.health.harm,
        )
        self.color = Color(
            self.colorSensor,
            self._setIsProtected,
            self.health.harm,
            self.health.heal,
            self._onOneSecondUpdate,
        )
        self._eventLoopRefreshRate = eventLoopRefreshRate
        self._accumulatedTime = 0

    def _setIsProtected(self, value: bool):
        self.isProtected = value

    def _onOneSecondUpdate(self, cb: "Callable[[], None]"):
        if self._accumulatedTime >= 1000:
            self._accumulatedTime = 0
            cb()
        else:
            self._accumulatedTime += self._eventLoopRefreshRate
