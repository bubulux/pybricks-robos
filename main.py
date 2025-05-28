from pybricks.parameters import Port
from pybricks.pupdevices import Motor
from pybricks.tools import wait

motor = Motor(Port.A)

while True:
    motor.run(200)

# wait(10 * 1000)
