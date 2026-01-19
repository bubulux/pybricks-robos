from pybricks.parameters import Direction, Port
from pybricks.iodevices import XboxController
from pybricks.pupdevices import Motor
from pybricks.tools import wait

from common.movement.index import Movement
from common.controller.index import Controller


leftMotor = Motor(
    Port.A,
)
rightMotor = Motor(Port.B, Direction.COUNTERCLOCKWISE)
body = Motor(Port.D)

movement = Movement(leftMotor, rightMotor)
controller = Controller(XboxController())


body.run_target(300, 0)

while True:
    wait(100)

    if controller.dPadNeutral():
        body.stop()
    elif controller.dPadRight():
        body.run(300)
    elif controller.dPadLeft():
        body.run(-300)

    isForward, forwardPercent = controller.forward()
    isBackward, backwardPercent = controller.backward()
    tiltDirection, tiltPercent = controller.tilt()

    movement.control.listenForBehavior(
        isForward,
        forwardPercent,
        isBackward,
        backwardPercent,
        tiltDirection,
        tiltPercent,
    )
