from utils.streamer import streamHealth


class Health:
    healthpoints = 100

    def check(self):
        if self.healthpoints <= 0:
            return False
        else:
            return True

    def harm(self, damage: int):
        self.healthpoints -= damage
        streamHealth(self.healthpoints)

    def heal(self, points: int):
        self.healthpoints += points
        streamHealth(self.healthpoints)
