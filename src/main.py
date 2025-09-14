from pybricks.hubs import PrimeHub
from pybricks.iodevices import XboxController
from pybricks.parameters import Direction, Port
from pybricks.pupdevices import ColorSensor, ForceSensor, Motor
from pybricks.tools import wait


from core.index import Core
from io.controller import Controller

from eventLoop import eventLoop


# Set up all devices.
hub = PrimeHub()
rightFeel = ForceSensor(Port.C)
leftFeel = ForceSensor(Port.D)
backFeel = ForceSensor(Port.A)
colorSensor = ColorSensor(Port.B)
rightMotor = Motor(Port.E, Direction.CLOCKWISE)
leftMotor = Motor(Port.F, Direction.COUNTERCLOCKWISE)
# XBoxController = XboxController()


core = Core(
    hub,
    rightFeel,
    leftFeel,
    backFeel,
    colorSensor,
    rightMotor,
    leftMotor,
)

# controller = Controller(XBoxController)

while True:
    eventLoop(core)
    wait(50)
