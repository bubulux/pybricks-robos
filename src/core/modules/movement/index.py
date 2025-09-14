from pybricks.pupdevices import Motor

from core.modules.movement.actions import Actions
from core.modules.movement.control import Control


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
            self._actions.stop,
            self._actions.forward,
            self._actions.backward,
            self._actions.turnLeft,
            self._actions.turnRight,
            self._actions.forwardLeft,
            self._actions.forwardRight,
            self._actions.backwardLeft,
            self._actions.backwardRight,
        )
