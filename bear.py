import random
import pygame


class Bear(object):
    BEAR_LIST = []
    BEAR_VELOCITY = 5
    BEAR_WIDTH = 100
    BEAR_HEIGHT = 100
    BEAR_IMG = pygame.transform.scale(
        pygame.image.load('Resources/Bear Trident.png'),
        (BEAR_WIDTH, BEAR_HEIGHT)
    )

    def __init__(self, window_width, windows_height, name):
        self.name = name
        self.bear_rect = pygame.Rect(
            random.randint(0, window_width - self.BEAR_WIDTH),
            windows_height - self.BEAR_HEIGHT,
            self.BEAR_WIDTH,
            self.BEAR_HEIGHT
        )
        self.right = True
        self.score = 0
        self.BEAR_LIST.append(self)

    def show(self, window):
        if self.right:
            window.blit(self.BEAR_IMG, (self.bear_rect.x, self.bear_rect.y))
        else:
            window.blit(pygame.transform.flip(self.BEAR_IMG, True, False), (self.bear_rect.x, self.bear_rect.y))

    def move(self, direction):
        self.bear_rect.x += self.BEAR_VELOCITY if direction == 'Right' else -1 * self.BEAR_VELOCITY
        self.right = True if direction == 'Right' else False

