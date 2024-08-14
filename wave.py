
from random import randint


class Wave:
    def __init__(self, make_enemy):
        self.enemies = []
        self.enemy_count = 0

        self.make_enemy = make_enemy

        self.random_wave(randint(1, 10))

    def random_wave(self, count):
        for _ in range(count):
            self.make_enemy()
            self.enemy_count += 1
