from typing import Callable, Literal

from pybricks.pupdevices import ForceSensor

from io.utils import forceToPercent


class Feeler:
    def __init__(
        self,
        sensorLeft: ForceSensor,
        sensorRight: ForceSensor,
        sensorBack: ForceSensor,
        harm: "Callable[[int], None]",
    ):
        self._sensorLeft = sensorLeft
        self._sensorRight = sensorRight
        self._sensorBack = sensorBack
        self._harm = harm

        self._lockLeft = 0

    def _damage(self, type: Literal["light", "medium", "heavy"]):
        if type == "light":
            self._harm(1)
        elif type == "medium":
            self._harm(3)
        elif type == "heavy":
            self._harm(6)

    def _proccessSensor(self, sensor: ForceSensor):

        percent = forceToPercent(sensor.force())

        if percent == 0 and self._lockLeft == 1:
            self._lockLeft = 0

        if self._lockLeft == 0:
            if 1 <= percent <= 30:
                self._damage("light")
                self._lockLeft = 1
            elif 31 <= percent <= 70:
                self._damage("medium")
                self._lockLeft = 1
            elif percent >= 71:
                self._damage("heavy")
                self._lockLeft = 1

    def listenForHits(self):
        self._proccessSensor(self._sensorLeft)
        pass
