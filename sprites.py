from settings import *


class Sprite(pygame.sprite.Sprite):
    def __init__(self, pos, image, groups):
        # noinspection PyTypeChecker
        super().__init__(groups)

        self.image = image
        self.rect = self.image.get_frect(topleft=pos)
        self.mask = pygame.mask.from_surface(self.image)


class AnimatedSprite(Sprite):
    def __init__(self, pos, frames, groups):
        super().__init__(pos, frames[0], groups)

        self.frames, self.frame_index = frames, 0

    def animate(self, dt):
        self.frame_index = (self.frame_index + ANIMATION_SPEED * dt) % len(self.frames)
        self.image = self.frames[self.frame_index]

    def update(self, dt):
        self.animate(dt)
