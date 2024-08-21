class Player:
    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id
        self.points = 0
        self.level = 1
        self.rewards = 0

    def add_points(self, points):
        self.points += points
        self.check_level()

    def check_level(self):
        if self.points >= 1000:
            self.level = 4
        elif self.points >= 500:
            self.level = 3
        elif self.points >= 100:
            self.level = 2
        else:
            self.level = 1

    def __str__(self):
        return f"{self.name} - Nivel: {self.level}, Puntos: {self.points}, Recompensas: {self.rewards}"
