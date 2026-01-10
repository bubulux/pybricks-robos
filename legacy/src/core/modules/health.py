from typing import Callable
from utils.streamer import streamHealth


class Health:

    def __init__(self, getIsProtected: Callable[[], bool]):
        self._getIsProtected = getIsProtected
        self.healthpoints = 100

    def check(self):
        if self.healthpoints <= 0:
            return False
        else:
            return True

    def harmWhileProtected(self, damage: int):
        self.healthpoints -= damage
        streamHealth(self.healthpoints)

    def harm(self, damage: int):
        if self._getIsProtected():
            return
        self.healthpoints -= damage
        streamHealth(self.healthpoints)

    def heal(self, points: int):
        if self.healthpoints + points > 100:
            self.healthpoints = 100
        else:
            self.healthpoints += points
        streamHealth(self.healthpoints)
