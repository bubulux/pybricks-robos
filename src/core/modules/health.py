from utils.streamer import streamHealth


class Health:

    def __init__(self, isProtected: bool):
        self._isProtected = isProtected

    healthpoints = 100

    def check(self):
        if self.healthpoints <= 0:
            return False
        else:
            return True

    def harmWhileProtected(self, damage: int):
        self.healthpoints -= damage
        streamHealth(self.healthpoints)

    def harm(self, damage: int):
        if self._isProtected:
            return
        self.healthpoints -= damage
        streamHealth(self.healthpoints)

    def heal(self, points: int):
        if self.healthpoints + points > 100:
            self.healthpoints = 100
        else:
            self.healthpoints += points
        streamHealth(self.healthpoints)
