from typing import Literal, Callable


class Control:

    def __init__(
        self,
        stop: "Callable[[], None]",
        forward: "Callable[[int], None]",
        backward: "Callable[[int], None]",
        turnLeft: "Callable[[int], None]",
        turnRight: "Callable[[int], None]",
        forwardLeft: "Callable[[int, int], None]",
        forwardRight: "Callable[[int, int], None]",
        backwardLeft: "Callable[[int, int], None]",
        backwardRight: "Callable[[int, int], None]",
    ):

        self._stop = stop
        self._forward = forward
        self._backward = backward
        self._turnLeft = turnLeft
        self._turnRight = turnRight
        self._forwardLeft = forwardLeft
        self._forwardRight = forwardRight
        self._backwardLeft = backwardLeft
        self._backwardRight = backwardRight

    def controlledBehavior(
        self,
        isForward: bool,
        forwardPercent: int,
        isBackward: bool,
        backwardPercent: int,
        tiltDirection: Literal["left", "right", "neutral"],
        tiltPercent: int,
    ):
        if not isForward and not isBackward and tiltDirection == "neutral":
            self._stop()
            return

        if isForward and isBackward:
            if tiltDirection == "left":
                self._turnLeft(tiltPercent)
                return
            elif tiltDirection == "right":
                self._turnRight(tiltPercent)
                return
            else:
                self._stop()
                return

        if isForward:
            if tiltDirection == "left":
                self._forwardLeft(forwardPercent, tiltPercent)
            elif tiltDirection == "right":
                self._forwardRight(forwardPercent, tiltPercent)
            else:
                self._forward(forwardPercent)
        elif isBackward:
            if tiltDirection == "left":
                self._backwardLeft(backwardPercent, tiltPercent)
            elif tiltDirection == "right":
                self._backwardRight(backwardPercent, tiltPercent)
            else:
                self._backward(backwardPercent)
