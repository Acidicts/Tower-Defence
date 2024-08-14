import pygame

from sprites import Sprite


class Projectile(Sprite):
    def __init__(self, pos, target, speed, groups):

        self.img = pygame.Surface((10, 10))
        self.img.fill((255, 255, 0))

        super().__init__(pos, img, groups)

        self.direction = Vector2()
        self.direction.x = target.centerx / self.rect.centerx
        self.direction.y = target.centery / self.rect.centery

    def update(self, dt):
        self.rect.x -= self.direction.x * dt * self.speed
        self.rect.y -= self.direction.y * dt * self.speed
