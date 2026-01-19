from pybricks.hubs import PrimeHub
from pybricks.parameters import Direction, Port
from pybricks.iodevices import XboxController
from pybricks.pupdevices import Motor
from pybricks.tools import wait

from common.movement.index import Movement
from common.controller.index import Controller

hub = PrimeHub(broadcast_channel=1)

leftMotor = Motor(
    Port.A,
)
rightMotor = Motor(Port.B, Direction.COUNTERCLOCKWISE)
body = Motor(Port.D)

controllerO = XboxController()


movement = Movement(leftMotor, rightMotor)
controller = Controller(controllerO)


body.run_target(300, 0)

while True:
    wait(100)

    if controller.dPadNeutral():
        body.stop()
        hub.ble.broadcast("neutral")
    if controller.dPadUp():
        hub.ble.broadcast("up")
    elif controller.dPadRight():
        body.run(300)
    elif controller.dPadDown():
        hub.ble.broadcast("down")
    elif controller.dPadLeft():
        body.run(-300)

    if controller.isPressedA():
        hub.ble.broadcast("reset")

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
