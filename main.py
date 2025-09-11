from pybricks.hubs import PrimeHub
from pybricks.parameters import Direction, Port
from pybricks.pupdevices import ColorSensor, ForceSensor, Motor
from pybricks.tools import wait

# Set up all devices.
prime_hub = PrimeHub()
right_feel = ForceSensor(Port.C)
left_feel = ForceSensor(Port.D)
back_feel = ForceSensor(Port.A)
color_sensor = ColorSensor(Port.B)
right = Motor(Port.E, Direction.CLOCKWISE)
left = Motor(Port.F, Direction.CLOCKWISE)


# The main program starts here.

# right.run(500)
# left.run(500)

def display_pixel():
    prime_hub.display.pixel()

while True:
    # print(f"Color: {color_sensor.hsv()}")
    # print(f"Right PRESSED: {right_feel.pressed()}")
    # print(f"Right TOUCHED: {right_feel.touched()}")
    # print(f"Left PRESSED: {left_feel.pressed()}")
    # print(f"Left TOUCHED: {left_feel.touched()}")
    # print(f"Back PRESSED: {back_feel.pressed()}")
    # print(f"Back TOUCHED: {back_feel.touched()}")
    wait(1000)
    pass