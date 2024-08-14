import pygame.key

from random import randint
from enemies import Enemy
from towers import Tower
from settings import *
from wave import Wave
from map import Map


class Level:
    def __init__(self):
        self.all_sprites = YSortGroup()
        self.towers = pygame.sprite.Group()
        self.paths = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()

        self.bullet_sprites = pygame.sprite.Group()

        self.map = Map([(-50, 100), (0, 100), (200, 100), (200, 300), (600, 300), (800, 500)])

        self.selected_tower = None
        self.draw = False

        self.wave = Wave(self.make_enemy)

    def make_enemy(self):
        Enemy((self.all_sprites, self.enemies), self.map.points)

    def run(self, dt):
        if self.enemies.sprites().__len__() == 0:
            self.wave.random_wave(randint(1, 10))

        self.map.draw(pygame.display.get_surface())

        keys = pygame.key.get_just_released()
        temp = Tower((pygame.mouse.get_pos()), None, (self.all_sprites, self.towers), self.enemies, 1000, (self.all_sprites, self.bullet_sprites))

        if keys[pygame.K_i]:
            offset = (temp.rect.x - self.map.map.get_rect().x, temp.rect.y - self.map.map.get_rect().y)

            if self.map.mask.overlap_area(temp.mask, offset):
                temp.kill()
            else:
                self.towers.add(temp)
        else:
            temp.kill()

        if keys[pygame.K_s]:
            self.draw = not self.draw

        self.all_sprites.custom_draw()
        self.all_sprites.update(dt)

        for bullet in self.bullet_sprites.sprites():
            for enemy in self.enemies.sprites():
                if bullet.rect.colliderect(enemy.rect):
                    bullet.kill()
                    enemy.die()

        win = pygame.display.get_surface()

        if self.draw:
            win.blit(self.map.mask.to_surface(), (0, 0))
            win.blit(self.all_sprites.sprites()[1].mask.to_surface(), temp.rect)


class YSortGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()

    def custom_draw(self):
        display = pygame.display.get_surface()

        for sprite in sorted(self.sprites(), key=lambda x: x.rect.y):
            display.blit(sprite.image, sprite.rect)
