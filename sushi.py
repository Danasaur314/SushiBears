import pygame
import random


class Sushi(object):
    MUNCH = pygame.mixer.Sound("Resources/Munch Sound Effect.wav")
    SUSHI_LIST = []
    SUSHI_WIDTH = 20
    SUSHI_HEIGHT = 20
    SUSHI_VELOCITY_Y = 6

    def __init__(self, window_width, window_height):
        self.sushi_rect = pygame.Rect(
            random.randint(0, window_width - self.SUSHI_WIDTH),
            0,
            self.SUSHI_WIDTH,
            self.SUSHI_HEIGHT
        )
        self.sushi_img = pygame.transform.scale(
            pygame.image.load(f'Resources/sushi{random.randint(1, 3)}.png'),
            (self.SUSHI_WIDTH, self.SUSHI_HEIGHT)
        )
        self.max_y = window_height
        self.SUSHI_LIST.append(self)

    def show(self, window):
        window.blit(self.sushi_img, (self.sushi_rect.x, self.sushi_rect.y))

    def update(self, check_collide):
        self.sushi_rect.y += self.SUSHI_VELOCITY_Y

        # Remove sushi if sushi left the screen (avoid blitting out-of-screen sushis)
        if self.sushi_rect.y > self.max_y:
            self.SUSHI_LIST.remove(self)
            return

        # Detect collision with bears (and adjust score)
        for bear in check_collide:
            if self.sushi_rect.colliderect(bear.bear_rect):
                self.MUNCH.play()
                self.SUSHI_LIST.remove(self)
                bear.score += 1
                break

