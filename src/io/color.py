from typing import Callable, Literal
from pybricks.pupdevices import ColorSensor

# Red == FORBIDDEN
# Green == HEALING
# Yellow == PROTECTED
# Orange == DAMAGING
# White == NEUTRAL


class Color:
    def __init__(
        self,
        colorSensor: ColorSensor,
        harm: "Callable[[int], None]",
        heal: "Callable[[int], None]",
        onOneSecondUpdate: "Callable[[Callable[[], None]], None]",
    ):
        self._colorSensor = colorSensor
        self._harm = harm
        self._heal = heal
        self._onOneSecondUpdate = onOneSecondUpdate

    def _colorToState(self, hue: int, saturation: int, value: int):
        return "FORBIDDEN"
        # return "HEALING"
        # return "PROTECTED"
        # return "DAMAGING"
        # return "NEUTRAL"

    def _execStateEffect(
        self,
        state: Literal[
            "FORBIDDEN", "HEALING", "PROTECTED", "DAMAGING", "NEUTRAL", "START"
        ],
    ):
        if state == "FORBIDDEN":
            self._harm(1)
        elif state == "HEALING":
            self._heal(5)
        elif state == "PROTECTED":
            pass
        elif state == "DAMAGING":
            self._harm(3)
        elif state == "NEUTRAL":
            pass
        elif state == "START":
            pass

    def _updateCallBack(self):
        hue, saturation, value = self._colorSensor.hsv()
        state = self._colorToState(hue, saturation, value)
        print(state)
        self._execStateEffect(state)

    def listenForStateUpdates(self):
        self._onOneSecondUpdate(self._updateCallBack)
