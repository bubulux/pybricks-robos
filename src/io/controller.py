from pybricks.iodevices import XboxController


class Controller:
    def __init__(self, controller: XboxController):
        self._controller = controller

    def shortRumble(self):
        self._controller.rumble(200)

    def forward(self):
        val = self._controller.triggers()[1]
        if val == 0:
            return (False, 0)
        return (True, val // 2)

    def backward(self):
        val = self._controller.triggers()[0]
        if val == 0:
            return (False, 0)
        return (True, val // 2)

    def tilt(self):
        horizontalVal = self._controller.joystick_left()[0]
        if horizontalVal > 0:
            return ("right", horizontalVal // 2)
        elif horizontalVal < 0:
            return ("left", abs(horizontalVal) // 2)
        else:
            return ("neutral", 0)
