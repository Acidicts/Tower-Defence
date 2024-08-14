import pygame

from sprites import Sprite
from settings import Vector2


class Projectile(Sprite):
    def __init__(self, pos, target, speed, groups):

        img = pygame.Surface((10, 10))
        img.fill((255, 255, 0))

        super().__init__(pos, img, groups)

        self.speed = speed

        self.direction = Vector2(target.centerx - self.rect.centerx, target.centery - self.rect.centery)
        self.direction.normalize_ip()

    def update(self, dt):
        self.rect.x += self.direction.x * self.speed * dt
        self.rect.y += self.direction.y * self.speed * dt