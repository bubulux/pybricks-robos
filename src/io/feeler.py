from typing import Callable, Literal

from pybricks.pupdevices import ForceSensor

from io.utils import forceToPercent, Mutex


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

        # Create mutex locks for each sensor
        self._lockLeft = Mutex()
        self._lockRight = Mutex()
        self._lockBack = Mutex()

    def _damage(self, type: Literal["light", "medium", "heavy"]):
        if type == "light":
            self._harm(5)
        elif type == "medium":
            self._harm(10)
        elif type == "heavy":
            self._harm(20)

    def _proccessSensor(self, sensor: ForceSensor, lock: Mutex):
        percent = forceToPercent(sensor.force())

        # If force is 0 and lock is active, release it
        if percent == 0 and lock.isLocked():
            lock.unlock()

        # Only process damage if lock is not active
        if not lock.isLocked():
            if 1 <= percent <= 30:
                self._damage("light")
                lock.lock()
            elif 31 <= percent <= 60:
                self._damage("medium")
                lock.lock()
            elif percent >= 61:
                self._damage("heavy")
                lock.lock()

    def listenForHits(self):
        self._proccessSensor(self._sensorLeft, self._lockLeft)
        self._proccessSensor(self._sensorRight, self._lockRight)
        self._proccessSensor(self._sensorBack, self._lockBack)
