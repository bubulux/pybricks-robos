from typing import Callable
from pybricks.pupdevices import ColorSensor

# Red == OUT_OF_BOUNDS
# Green == HEALING
# Yellow == PROTECTED
# Orange == DAMAGING
# White == NEUTRAL

# Utility for translating color sensor readings into game states
# Utility for updating via 1 second interval, needs to be based in the 50ms event loop


class Color:
    def __init__(
        self,
        colorSensor: ColorSensor,
        harm: "Callable[[int], None]",
        heal: "Callable[[int], None]",
    ):
        self._colorSensor = colorSensor

    def _getColor(self):
        return self._colorSensor.hsv()

    def _getState(self):
        pass

    def scanForColorFields(self):
        pass
