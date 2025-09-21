from core.index import Core
from pybricks.tools import wait

from io.controller import Controller
from utils.streamer import streamEnd, streamStart


class EventLoop:
    def __init__(self, core: Core, controller: Controller, refreshRate: int):
        self._core = core
        self._controller = controller
        self._refreshRate = refreshRate

    def _roboLoop(self):
        isForward, forwardPercent = self._controller.forward()
        isBackward, backwardPercent = self._controller.backward()
        tiltDirection, tiltPercent = self._controller.tilt()

        self._core.movement.control.listenForBehavior(
            isForward,
            forwardPercent,
            isBackward,
            backwardPercent,
            tiltDirection,
            tiltPercent,
        )
        self._core.feeler.listenForHits()
        self._core.color.listenForState()

        return self._core.health.check()

    def run(self):

        streamStart()

        while True:
            isAlive = self._roboLoop()

            if not isAlive:
                streamEnd()
                break

            wait(self._refreshRate)
