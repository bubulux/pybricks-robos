from core.index import Core
from io.controller import Controller
from pybricks.tools import wait


def eventLoop(
    core: Core,
    refreshRate: int,
):

    # isForward, forwardPercent = controller.forward()
    # isBackward, backwardPercent = controller.backward()
    # tiltDirection, tiltPercent = controller.tilt()

    # core.movement.control.controlledBehavior(
    #     isForward,
    #     forwardPercent,
    #     isBackward,
    #     backwardPercent,
    #     tiltDirection,
    #     tiltPercent,
    # )

    # core.feeler.listenForHits()
    # core.health.check()
    core.color.listenForStateUpdates()
    wait(refreshRate)
