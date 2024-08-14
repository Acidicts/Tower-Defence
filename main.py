from settings import *
from level import Level


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Tower Defense")

        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.running = True

        self.level = Level()

        self.clock = pygame.time.Clock()

    def run(self):
        while self.running:
            self.clock.tick()
            dt = self.clock.get_fps() / 1000
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.screen.fill((50, 150, 30))

            self.level.run(dt)

            pygame.display.flip()

        pygame.quit()


if __name__ == '__main__':
    Game().run()
