from typing import Callable, Literal
from pybricks.pupdevices import ColorSensor

from utils.streamer import streamLightState


class Color:
    def __init__(
        self,
        colorSensor: ColorSensor,
        setIsProtected: "Callable[[bool], None]",
        harm: "Callable[[int], None]",
        heal: "Callable[[int], None]",
        onOneSecondUpdate: "Callable[[Callable[[], None]], None]",
    ):
        self._colorSensor = colorSensor
        self._harm = harm
        self._heal = heal
        self._onOneSecondUpdate = onOneSecondUpdate
        self._setIsProtected = setIsProtected

    def _colorToState(self, hue: int, saturation: int, value: int):

        # Red == FORBIDDEN
        # Green == HEALING
        # Yellow == PROTECTED
        # Orange == DAMAGING
        # White == NEUTRAL
        # Blue == WIN

        # return "FORBIDDEN"
        # return "HEALING"
        # return "PROTECTED"
        # return "DAMAGING"#
        # return "WIN"
        return "NEUTRAL"

    def _execStateEffect(
        self,
        state: Literal[
            "FORBIDDEN", "HEALING", "PROTECTED", "DAMAGING", "NEUTRAL", "START", "WIN"
        ],
    ):
        if state == "FORBIDDEN":
            self._setIsProtected(False)
            streamLightState("FORBIDDEN")
            self._harm(20)
        elif state == "HEALING":
            self._setIsProtected(False)
            streamLightState("HEALING")
            self._heal(5)
        elif state == "PROTECTED":
            self._setIsProtected(True)
            streamLightState("PROTECTED")
        elif state == "DAMAGING":
            self._setIsProtected(False)
            streamLightState("DAMAGING")
            self._harm(3)
        elif state == "NEUTRAL":
            self._setIsProtected(False)
            streamLightState("NEUTRAL")
        elif state == "WIN":
            streamLightState("WIN")

    def _updateCallBack(self):
        hue, saturation, value = self._colorSensor.hsv()
        state = self._colorToState(hue, saturation, value)
        self._execStateEffect(state)

    def listenForState(self):
        self._onOneSecondUpdate(self._updateCallBack)
