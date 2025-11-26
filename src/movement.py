from pybricks.hubs import PrimeHub
from pybricks.parameters import Direction, Port
from pybricks.pupdevices import Motor

hub = PrimeHub()
rightMotor = Motor(Port.D)
leftMotor = Motor(Port.C, Direction.COUNTERCLOCKWISE)

schritt = 270


def schrittVorwaerts():
    rightMotor.run_angle(speed=200, rotation_angle=schritt, wait=False)
    leftMotor.run_angle(speed=200, rotation_angle=schritt, wait=True)


def schrittRueckwaerts():
    rightMotor.run_angle(speed=-200, rotation_angle=schritt, wait=False)
    leftMotor.run_angle(speed=-200, rotation_angle=schritt, wait=True)


def drehungLinks():
    rightMotor.run_angle(speed=200, rotation_angle=180, wait=False)
    leftMotor.run_angle(speed=-200, rotation_angle=180, wait=True)


def drehungRechts():
    rightMotor.run_angle(speed=-200, rotation_angle=180, wait=False)
    leftMotor.run_angle(speed=200, rotation_angle=180, wait=True)


def abliefern():
    hub.speaker.beep(duration=1000)
