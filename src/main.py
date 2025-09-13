from pybricks.hubs import PrimeHub
from pybricks.parameters import Direction, Port
from pybricks.pupdevices import ColorSensor, ForceSensor, Motor

from core.index import Core


# Set up all devices.
hub = PrimeHub()
rightFeel = ForceSensor(Port.C)
leftFeel = ForceSensor(Port.D)
backFeel = ForceSensor(Port.A)
colorSensor = ColorSensor(Port.B)
rightMotor = Motor(Port.E, Direction.COUNTERCLOCKWISE)
leftMotor = Motor(Port.F, Direction.CLOCKWISE)


core = Core(
    hub,
    rightFeel,
    leftFeel,
    backFeel,
    colorSensor,
    rightMotor,
    leftMotor,
)

while True:

    core.movement.forward(10)

    pass
