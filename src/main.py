from pybricks.hubs import PrimeHub
from pybricks.iodevices import XboxController
from pybricks.parameters import Direction, Port
from pybricks.pupdevices import ColorSensor, ForceSensor, Motor
from pybricks.tools import wait


from core.index import Core
from io.controller import Controller


# Set up all devices.
hub = PrimeHub()
rightFeel = ForceSensor(Port.C)
leftFeel = ForceSensor(Port.D)
backFeel = ForceSensor(Port.A)
colorSensor = ColorSensor(Port.B)
rightMotor = Motor(Port.E, Direction.CLOCKWISE)
leftMotor = Motor(Port.F, Direction.COUNTERCLOCKWISE)
XBoxController = XboxController()


core = Core(
    hub,
    rightFeel,
    leftFeel,
    backFeel,
    colorSensor,
    rightMotor,
    leftMotor,
)

controller = Controller(XBoxController)

while True:

    isForward, forwardPercent = controller.forward()
    isBackward, backwardPercent = controller.backward()
    tiltDirection, tiltPercent = controller.tilt()

    if not isForward and not isBackward and tiltDirection == "neutral":
        core.movement.stop()
        continue

    if isForward and isBackward:
        if tiltDirection == "left":
            core.movement.turnLeft(tiltPercent)
            continue
        elif tiltDirection == "right":
            core.movement.turnRight(tiltPercent)
            continue
        else:
            core.movement.stop()
            continue

    if isForward:
        if tiltDirection == "left":
            core.movement.forwardLeft(forwardPercent, tiltPercent)
        elif tiltDirection == "right":
            core.movement.forwardRight(forwardPercent, tiltPercent)
        else:
            core.movement.forward(forwardPercent)
    elif isBackward:
        if tiltDirection == "left":
            core.movement.backwardLeft(backwardPercent, tiltPercent)
        elif tiltDirection == "right":
            core.movement.backwardRight(backwardPercent, tiltPercent)
        else:
            core.movement.backward(backwardPercent)

    wait(50)
    pass
