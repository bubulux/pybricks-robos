from pybricks.hubs import PrimeHub
from pybricks.parameters import Direction, Port
from pybricks.pupdevices import ColorSensor, ForceSensor, Motor
from pybricks.tools import wait
from pybricks.iodevices import XboxController

# Set up all devices.
prime_hub = PrimeHub()
right_feel = ForceSensor(Port.C)
left_feel = ForceSensor(Port.D)
back_feel = ForceSensor(Port.A)
color_sensor = ColorSensor(Port.B)
right = Motor(Port.E, Direction.COUNTERCLOCKWISE)
left = Motor(Port.F, Direction.CLOCKWISE)
controller = XboxController()


# The main program starts here.

# right.run(500)
# left.run(500)

# def display_pixel():
#     prime_hub.display.pixel(0,0,100)

# display_pixel()

def isForward():
    lt = controller.triggers()[0]
    if lt > 0:
        return True
    return False

def isBackward():
    rt = controller.triggers()[1]
    if rt > 0:
        return True
    return False

def isStop():
    if isForward() == False and isBackward() == False:
        return True

def runForward():
    print("Running forward")
    left.run(500)
    right.run(500)

def runBackward():
    print("Running backward")
    left.run(-500)
    right.run(-500)

while True:
    if isForward():
        runForward()
    elif isBackward():
        runBackward()
    elif isStop():
        left.stop()
        right.stop()
    wait(50)
    pass