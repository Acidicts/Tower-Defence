import pygame.math

from sprites import *
from projectiles import Projectile


class Tower(Sprite):
    def __init__(self, pos, image, groups, enemies, cooldown, projectiles):
        if not image:
            image = pygame.surface.Surface((64, 64))
            image.fill((255, 0, 0))

        super().__init__(pos, image, groups)

        self.enemies = enemies
        self.target = None

        self.cooldown = cooldown
        self.time = None

        self.projectile_groups = projectiles

        self.vecs = {
            'tower': Vector2(self.rect.center),
            'enemy': None
        }

    def retarget(self):
        m = 1000
        self.target = None
        for enemy in self.enemies:
            e_vec = pygame.math.Vector2(enemy.rect.center)
            t_vec = pygame.math.Vector2(self.rect.center)

            if e_vec.distance_to(t_vec) < m:
                m = e_vec.distance_to(t_vec)
                self.target = enemy

        if self.target:
            self.vecs = {
                'tower': Vector2(self.rect.center),
                'enemy': Vector2(self.target.rect.center)
            }
        else:
            self.target = None
            self.vecs = {
                'tower': Vector2(self.rect.center),
                'enemy': None
            }

    def attack(self):

        self.retarget()

        if self.target and self.enemies.sprites().__len__() > 0:
            if not self.time:
                self.time = pygame.time.get_ticks()
                Projectile(self.rect.center, self.target.rect, 30, self.projectile_groups)
            else:
                if pygame.time.get_ticks() - self.time >= self.cooldown:
                    self.time = None

    def update(self, dt):
        self.attack()
