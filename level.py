from settings import *
from map import Map


class Level:
    def __init__(self):
        self.all_sprites = YSortGroup()
        self.towers = pygame.sprite.Group()
        self.paths = pygame.sprite.Group()

        self.map = Map([(0, 100), (200, 100), (200, 300), (600, 300), (800, 500)])

    def run(self):
        self.map.draw(pygame.display.get_surface())

        self.all_sprites.custom_draw()


class YSortGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()

    def custom_draw(self):
        display = pygame.display.get_surface()

        for sprite in sorted(self.sprites(), key=lambda x: x.rect.y):
            display.blit(sprite.image, sprite.rect)
