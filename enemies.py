import pygame

from sprites import Sprite
from random import randint


class Enemy(Sprite):
    def __init__(self, groups, map_points):

        image = pygame.Surface((32, 32))
        image.fill((0, 0, 255))

        super().__init__(map_points[0], image, groups)
        self.points = map_points
        self.health = 2
        self.speed = 5

        self.wait = False

    def move(self, dt):
        if self.wait:
            if self.points:
                if self.rect.collidepoint(self.points[0]):
                    self.points.pop(0)
                else:
                    vec = pygame.math.Vector2(self.points[0]) - pygame.math.Vector2(self.rect.center)
                    vec.normalize_ip()
                    vec *= self.speed * dt
                    self.rect.move_ip(vec)
            else:
                self.kill()

    def die(self):
        if self.wait:
            self.kill()

    def update(self, dt):
        if self.health <= 0:
            self.kill()
        else:
            self.move(dt)

        if randint(0, 10000) <= 5:
            self.wait = True

