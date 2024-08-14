from settings import *


class Map:
    def __init__(self, points):
        self.points = points

    def draw(self, display):
        for i in range(len(self.points) - 1):
            if self.points[i][0] == self.points[i + 1][0] or self.points[i][1] == self.points[i + 1][1]:
                pygame.draw.line(display, (200, 100, 100), self.points[i], self.points[i + 1], 50)
                pygame.draw.rect(display, (200, 100, 100), (self.points[i][0] - 25, self.points[i][1] - 25, 50, 50))
            else:
                pygame.draw.line(display, (200, 100, 100), self.points[i], self.points[i+1], 100)
                pygame.draw.rect(display, (200, 100, 100), (self.points[i][0] - 25, self.points[i][1] - 25, 75, 50))
