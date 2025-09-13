class Health:
    healthpoints = 1000

    def check(self):
        if self.healthpoints <= 0:
            print("ROBOT: NO_POINTS")
            return False
        else:
            print(f"HEALTH_INDICATOR: {self.healthpoints}")
            return True

    def harm(self, damage: int):
        self.healthpoints -= damage

    def heal(self, points: int):
        self.healthpoints += points
