from pybricks.iodevices import XboxController


class Controller:
    def __init__(self, controller: XboxController):
        self._controller = controller

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
            return ("right", horizontalVal)
        elif horizontalVal < 0:
            return ("left", abs(horizontalVal))
        else:
            return ("neutral", 0)
