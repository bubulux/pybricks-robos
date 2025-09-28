from utils.streamer import streamHealth


class Health:

    def __init__(self, isProtected: bool):
        self.isProtected = isProtected

    healthpoints = 100

    def check(self):
        if self.healthpoints <= 0:
            return False
        else:
            return True

    def harm(self, damage: int):
        if self.isProtected:
            return
        self.healthpoints -= damage
        streamHealth(self.healthpoints)

    def heal(self, points: int):
        self.healthpoints += points
        streamHealth(self.healthpoints)
