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

        self._debouncer = 0

    def _damage(self, type: Literal["light", "medium", "heavy"]):
        if type == "light":
            self._harm(1)
        elif type == "medium":
            self._harm(3)
        elif type == "heavy":
            self._harm(6)

    def _propagateHit(
        self,
        sensor: ForceSensor,
        forPressed: Literal["light", "medium", "heavy"],
        forTouched: Literal["light", "medium", "heavy"],
    ):
        if sensor.pressed():
            self._damage(forPressed)
        if sensor.touched():
            self._damage(forTouched)

    def _applyHits(self):
        self._propagateHit(self._sensorLeft, "medium", "light")
        self._propagateHit(self._sensorRight, "medium", "light")
        self._propagateHit(self._sensorBack, "heavy", "medium")

    def fillDebounce(self):
        self._debouncer = self._debouncer + 50

    def resetDebounce(self):
        self._debouncer = 0

    def listenForHits(self):
        if self._debouncer == 250:
            self._applyHits()
            self.resetDebounce()
        else:
            self.fillDebounce()
