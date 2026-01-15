from pybricks.parameters import Direction, Port
from pybricks.iodevices import XboxController
from pybricks.pupdevices import Motor

leftMotor = Motor(Port.A, Direction.COUNTERCLOCKWISE)
rightMotor = Motor(Port.B)
controller = XboxController()


body = Motor(Port.D)
