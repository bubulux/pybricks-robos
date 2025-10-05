from pybricks.hubs import PrimeHub
from pybricks.iodevices import XboxController
from pybricks.parameters import Direction, Port
from pybricks.pupdevices import ColorSensor, ForceSensor, Motor


from core.index import Core
from io.controller import Controller

from eventLoop import EventLoop


# Set up all devices.
hub = PrimeHub()
rightFeel = ForceSensor(Port.C)
leftFeel = ForceSensor(Port.D)
backFeel = ForceSensor(Port.A)
colorSensor = ColorSensor(Port.B)
rightMotor = Motor(Port.E, Direction.CLOCKWISE)
leftMotor = Motor(Port.F, Direction.COUNTERCLOCKWISE)
XBoxController = XboxController()

refreshRate = 50  # milliseconds

controller = Controller(XBoxController)

core = Core(
    refreshRate,
    controller.shortRumble,
    hub,
    rightFeel,
    leftFeel,
    backFeel,
    colorSensor,
    rightMotor,
    leftMotor,
)


EventLoop(core, controller, refreshRate).run()
