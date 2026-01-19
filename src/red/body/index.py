from pybricks.hubs import PrimeHub
from pybricks.parameters import Direction, Port
from pybricks.pupdevices import Motor
from pybricks.tools import wait

hub = PrimeHub(observe_channels=[1])
leftArm = Motor(
    Port.A,
)
rightArm = Motor(Port.B, Direction.COUNTERCLOCKWISE)

leftArm.run_target(300, 0)
rightArm.run_target(300, 0)

while True:
    wait(100)
    # "up", "down", or "neutral"
    data = hub.ble.observe(1)  # type: ignore

    if data == "up":  # type: ignore
        leftArm.run(300)
        rightArm.run(300)
    elif data == "down":  # type: ignore
        leftArm.run(-300)
        rightArm.run(-300)
    elif data == "neutral":  # type: ignore
        leftArm.stop()
        rightArm.stop()
    elif data == "reset":  # type: ignore
        leftArm.run_target(300, 0)
        rightArm.run_target(300, 0)
