from typing import Callable, Literal
from pybricks.pupdevices import ColorSensor

from utils.streamer import streamLightState


class Color:
    def __init__(
        self,
        colorSensor: ColorSensor,
        setIsProtected: "Callable[[bool], None]",
        harm: "Callable[[int], None]",
        harmWhileProtected: "Callable[[int], None]",
        heal: "Callable[[int], None]",
        onOneSecondUpdate: "Callable[[Callable[[], None]], None]",
    ):
        self._colorSensor = colorSensor
        self._harm = harm
        self._harmWhileProtected = harmWhileProtected
        self._heal = heal
        self._onOneSecondUpdate = onOneSecondUpdate
        self._setIsProtected = setIsProtected

    def _hsvToColor(self, hue: int, saturation: int, value: int) -> Literal[
        "YELLOW",
        "RED",
        "GREEN",
        "PINK",
        "BLUE",
        "WHITE",
        "BLACK",
    ]:
        # YELLOW = H: 49,52 S: 64, 69 V: 15 (PROTECTED)
        # RED = H: 350, 355 S: 92, 93 V: 9,11 (DAMAGING)
        # GREEN = H: 120, 132 S: 55,59,65 V: 7, 11 (HEALING)
        # PINK = H: 330,335 S: 75,77 V: 7,9 (PROTECTED-DAMAGING)
        # BLUE = H: 215,210  S: 93, 94  V: 5 (WIN)
        # WHITE = H: 200, 220 S: 20 V: 19 (NEUTRAL)
        # BLACK =  H: 210, S: 43, V: 5 (FORBIDDEN)

        if 40 <= hue <= 60 and 60 <= saturation <= 75 and 10 <= value <= 20:
            return "YELLOW"
        elif (hue >= 350 or hue <= 5) and 92 <= saturation <= 93 and 9 <= value <= 11:
            return "RED"
        elif 100 <= hue <= 110 and 55 <= saturation <= 65 and 7 <= value <= 11:
            return "GREEN"
        elif 330 <= hue <= 335 and 75 <= saturation <= 77 and 7 <= value <= 9:
            return "PINK"
        elif 210 <= hue <= 215 and 93 <= saturation <= 94 and value == 5:
            return "BLUE"
        elif 200 <= hue <= 220 and saturation == 20 and value == 19:
            return "WHITE"
        elif hue == 210 and saturation == 43 and value == 5:
            return "BLACK"
        else:
            return "WHITE"

    def _colorToState(
        self,
        color: Literal[
            "YELLOW",
            "RED",
            "GREEN",
            "PINK",
            "BLUE",
            "WHITE",
            "BLACK",
        ],
    ) -> Literal[
        "FORBIDDEN",
        "HEALING",
        "PROTECTED",
        "DAMAGING",
        "NEUTRAL",
        "PROTECTED-DAMAGING",
        "WIN",
    ]:

        if color == "YELLOW":
            return "PROTECTED"
        elif color == "RED":
            return "DAMAGING"
        elif color == "GREEN":
            return "HEALING"
        elif color == "PINK":
            return "PROTECTED-DAMAGING"
        elif color == "BLUE":
            return "WIN"
        elif color == "WHITE":
            return "NEUTRAL"
        elif color == "BLACK":
            return "FORBIDDEN"
        else:
            return "NEUTRAL"

    def _execStateEffect(
        self,
        state: Literal[
            "FORBIDDEN",
            "HEALING",
            "PROTECTED",
            "DAMAGING",
            "NEUTRAL",
            "START",
            "WIN",
            "PROTECTED-DAMAGING",
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
        elif state == "PROTECTED-DAMAGING":
            self._setIsProtected(True)
            streamLightState("PROTECTED-DAMAGING")
            self._harmWhileProtected(5)
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
        color = self._hsvToColor(hue, saturation, value)
        state = self._colorToState(color)
        self._execStateEffect(state)

    def listenForState(self):
        self._onOneSecondUpdate(self._updateCallBack)
