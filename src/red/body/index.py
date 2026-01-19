from pybricks.hubs import PrimeHub

hub = PrimeHub(observe_channels=[1])

while True:
    data = hub.ble.observe(1)  # type: ignore
    print("Received:", data)
