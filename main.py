from pybricks.parameters import Port, Direction
from pybricks.pupdevices import Motor
from pybricks.tools import wait

rightMotor = Motor(Port.A, Direction.COUNTERCLOCKWISE)
leftMotor = Motor(Port.E)

rightMotor.run(300)
leftMotor.run(300)

wait(3 * 1000)

rightMotor.run(-300)
leftMotor.run(-300)

wait(3 * 1000)

rightMotor.run(300)
leftMotor.run(-300)

wait(3 * 1000)
