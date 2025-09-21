from core.index import Core
from io.controller import Controller
from pybricks.tools import wait


class EventLoop:
    def __init__(self, core: Core, controller: Controller, refreshRate: int):
        self._core = core
        self._controller = controller
        self._refreshRate = refreshRate

    def _roboLoop(self):
        isForward, forwardPercent = self._controller.forward()
        isBackward, backwardPercent = self._controller.backward()
        tiltDirection, tiltPercent = self._controller.tilt()

        self._core.movement.control.controlledBehavior(
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
        while True:
            if not self._roboLoop():
                break
            wait(self._refreshRate)
