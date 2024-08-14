from settings import *
from level import Level


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Tower Defense")

        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.running = True

        self.level = Level()

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.screen.fill((50, 150, 30))

            self.level.run()

            pygame.display.flip()

        pygame.quit()


if __name__ == '__main__':
    Game().run()
