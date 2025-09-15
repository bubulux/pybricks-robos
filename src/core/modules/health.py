class Health:
    healthpoints = 100

    def check(self):
        if self.healthpoints <= 0:
            print("ROBOT: NO_POINTS")
            return False
        else:
            print(f"{self.healthpoints}, NONE, NONE, NONE, NONE")
            return True

    def harm(self, damage: int):
        self.healthpoints -= damage

    def heal(self, points: int):
        self.healthpoints += points
