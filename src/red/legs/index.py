from pybricks.hubs import PrimeHub
from pybricks.parameters import Direction, Port, Button
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

    # 1 UP
    # 7 LEFT
    # 3 RIGHT
    # 5 DOWN
    dPadDir = controllerO.dpad()
    button = controllerO.buttons

    if dPadDir == 0:
        body.stop()
        hub.ble.broadcast("neutral")
    if dPadDir == 1:
        hub.ble.broadcast("up")
    elif dPadDir == 3:
        body.run(300)
    elif dPadDir == 5:
        hub.ble.broadcast("down")
    elif dPadDir == 7:
        body.run(-300)

    if button.pressed() == {Button.A}:
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
