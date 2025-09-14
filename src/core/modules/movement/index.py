from typing import Literal
from pybricks.pupdevices import Motor

from core.modules.movement.actions import Actions


class Control:

    def __init__(
        self,
        actions: Actions,
    ):

        self._actions = actions

    def controlledBehavior(
        self,
        isForward: bool,
        forwardPercent: int,
        isBackward: bool,
        backwardPercent: int,
        tiltDirection: Literal["left", "right", "neutral"],
        tiltPercent: int,
    ):
        if not isForward and not isBackward and tiltDirection == "neutral":
            self._actions.stop()
            return

        if isForward and isBackward:
            if tiltDirection == "left":
                self._actions.turnLeft(tiltPercent)
                return
            elif tiltDirection == "right":
                self._actions.turnRight(tiltPercent)
                return
            else:
                self._actions.stop()
                return

        if isForward:
            if tiltDirection == "left":
                self._actions.forwardLeft(forwardPercent, tiltPercent)
            elif tiltDirection == "right":
                self._actions.forwardRight(forwardPercent, tiltPercent)
            else:
                self._actions.forward(forwardPercent)
        elif isBackward:
            if tiltDirection == "left":
                self._actions.backwardLeft(backwardPercent, tiltPercent)
            elif tiltDirection == "right":
                self._actions.backwardRight(backwardPercent, tiltPercent)
            else:
                self._actions.backward(backwardPercent)


class Movement:

    def __init__(
        self,
        rightMotor: Motor,
        leftMotor: Motor,
    ):
        self._rightMotor = rightMotor
        self._leftMotor = leftMotor

        self._actions = Actions(self._rightMotor, self._leftMotor)
        self.control = Control(
            self._actions,
        )
