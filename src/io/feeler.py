from typing import Callable, Literal

from pybricks.pupdevices import ForceSensor


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

    def _damage(self, type: Literal["light", "medium", "heavy"]):
        if type == "light":
            self._harm(5)
        elif type == "medium":
            self._harm(10)
        elif type == "heavy":
            self._harm(20)

    def propagateHit(
        self,
        sensor: ForceSensor,
        forPressed: Literal["light", "medium", "heavy"],
        forTouched: Literal["light", "medium", "heavy"],
    ):
        if sensor.pressed():
            self._damage(forPressed)
        if sensor.touched():
            self._damage(forTouched)

    def listenForHits(self):
        self.propagateHit(self._sensorLeft, "medium", "light")
        self.propagateHit(self._sensorRight, "medium", "light")
        self.propagateHit(self._sensorBack, "heavy", "medium")
