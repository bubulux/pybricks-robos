from pybricks.parameters import Direction, Port
from pybricks.iodevices import XboxController
from pybricks.pupdevices import Motor
from pybricks.tools import wait

leftMotor = Motor(Port.A, Direction.COUNTERCLOCKWISE)
rightMotor = Motor(Port.B)
body = Motor(Port.D)

controller = XboxController()


while True:
    wait(100)

    # 1 UP
    # 7 LEFT
    # 3 RIGHT
    # 5 DOWN
    dPadDir = controller.dpad()

    if dPadDir == 0:
        body.stop()
    if dPadDir == 1:
        pass
    elif dPadDir == 3:
        body.run(300)
    elif dPadDir == 5:
        pass
    elif dPadDir == 7:
        body.run(-300)

    # Movement
    forward = controller.triggers()[1]
    backward = controller.triggers()[0]

    if forward == 0 and backward == 0:
        leftMotor.stop()
        rightMotor.stop()

    if forward > 0:
        leftMotor.run(forward * 20)
        rightMotor.run(forward * 20)

    elif backward > 0:
        leftMotor.run(-backward * 20)
        rightMotor.run(-backward * 20)
