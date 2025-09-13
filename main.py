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


while True:
   
    pass