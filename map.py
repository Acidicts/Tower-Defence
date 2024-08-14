from settings import *


class Map:
    def __init__(self, points):
        self.points = points
        self.map = pygame.Surface((WIDTH, HEIGHT)).convert_alpha()
        self.map.fill((0, 0, 0))
        self.mask = None

    def draw(self, display):
        for i in range(len(self.points) - 1):
            if self.points[i][0] == self.points[i + 1][0] or self.points[i][1] == self.points[i + 1][1]:
                pygame.draw.line(self.map, (200, 100, 100), self.points[i], self.points[i + 1], 50)
                pygame.draw.rect(self.map, (200, 100, 100), (self.points[i][0] - 25, self.points[i][1] - 25, 50, 50))
            else:
                pygame.draw.line(self.map, (200, 100, 100), self.points[i], self.points[i+1], 100)
                pygame.draw.rect(self.map, (200, 100, 100), (self.points[i][0] - 25, self.points[i][1] - 25, 75, 50))

        self.map.set_colorkey((0, 0, 0))
        self.mask = pygame.mask.from_surface(self.map)
        display.blit(self.map, (0, 0))
