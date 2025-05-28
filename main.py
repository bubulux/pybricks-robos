from pybricks.hubs import PrimeHub
from pybricks.parameters import Color
from pybricks.tools import wait


hub = PrimeHub()
hub.light.on(Color.RED)
wait(2000)
print("I am", __name__)
hub.light.on(Color.GREEN)
wait(2000)