from pybricks.hubs import PrimeHub
from pybricks.parameters import Direction, Port
from pybricks.pupdevices import Motor

rightMotor = Motor(Port.D)
leftMotor = Motor(Port.C, Direction.COUNTERCLOCKWISE)

while True:
    rightMotor.run(500)
    leftMotor.run(500)
