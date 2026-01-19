from pybricks.iodevices import XboxController
from pybricks.parameters import Button


class Controller:
    def __init__(self, controller: XboxController):
        self._controller = controller

    def shortRumble(self):
        self._controller.rumble(200)

    def forward(self):
        val = self._controller.triggers()[1]
        if val == 0:
            return (False, 0)
        return (True, val)

    def backward(self):
        val = self._controller.triggers()[0]
        if val == 0:
            return (False, 0)
        return (True, val)

    def tilt(self):
        horizontalVal = self._controller.joystick_left()[0]
        if horizontalVal > 0:
            return ("right", horizontalVal // 2)
        elif horizontalVal < 0:
            return ("left", abs(horizontalVal) // 2)
        else:
            return ("neutral", 0)

    def dPadUp(self):
        return self._controller.dpad() == 1

    def dPadRight(self):
        return self._controller.dpad() == 3

    def dPadDown(self):
        return self._controller.dpad() == 5

    def dPadLeft(self):
        return self._controller.dpad() == 7

    def dPadNeutral(self):
        return self._controller.dpad() == 0

    def isPressedA(self):
        return Button.A in self._controller.buttons.pressed()

    def isPressedB(self):
        return Button.B in self._controller.buttons.pressed()

    def isPressedX(self):
        return Button.X in self._controller.buttons.pressed()

    def isPressedY(self):
        return Button.Y in self._controller.buttons.pressed()
