import pygame

# Init pygame before importing bear and sushi modules for sushi class sound effects
pygame.init()

import SushiBears.bear as bear
import SushiBears.sushi as sushi

WINDOW_WIDTH = 700
WINDOW_HEIGHT = 400
FPS = 60
SCORE_FONT = pygame.font.SysFont('comicsans', 40)
WINNER_FONT = pygame.font.SysFont('comicsans', 100)
BLACK = (0, 0, 0)
WINNING_SCORE = 10
WINNING_SCREEN_TIMEOUT_MILLISECONDS = 3000
SUSHI_CREATION = pygame.USEREVENT + 1
SUSHI_CREATION_INTERVAL_MILLISECONDS = 400
BEAR_SCORE_SCREEN_OFFSET = 10
BACKGROUND = pygame.transform.scale(
    pygame.image.load('Resources/Game Background.jpg'),
    (WINDOW_WIDTH, WINDOW_HEIGHT)
)


def check_for_winner(window, bear_list):
    for beari in bear_list:
        if beari.score >= WINNING_SCORE:
            show_winner(window, beari.name, bear_list[0], bear_list[1])


def show_winner(window, winner_name, bear_1, bear_2):
    winner_text = WINNER_FONT.render(f'{winner_name} won', 1, BLACK)
    winner_text_x = WINDOW_WIDTH // 2 - winner_text.get_width() // 2
    winner_text_y = WINDOW_HEIGHT // 2 - winner_text.get_height() // 2
    window.blit(winner_text, (winner_text_x, winner_text_y))

    pygame.display.update()
    pygame.time.delay(WINNING_SCREEN_TIMEOUT_MILLISECONDS)
    restart(bear_1, bear_2)


def restart(bear_1, bear_2):
    bear_1.score = 0
    bear_2.score = 0
    sushi.Sushi.SUSHI_LIST = []


def draw_window(window, bear_1, bear_2):
    # draws window, captions (score) and bears (players)
    window.blit(BACKGROUND, (0, 0))

    bear_1_score_text = SCORE_FONT.render(f"first bear score: {bear_1.score}", 1, BLACK)
    window.blit(
        bear_1_score_text,
        (WINDOW_WIDTH - bear_1_score_text.get_width() - BEAR_SCORE_SCREEN_OFFSET, BEAR_SCORE_SCREEN_OFFSET)
    )

    bear_2_score_text = SCORE_FONT.render(f"second bear score: {bear_2.score}", 1, BLACK)
    window.blit(bear_2_score_text, (BEAR_SCORE_SCREEN_OFFSET, BEAR_SCORE_SCREEN_OFFSET))

    bear_1.show(window)
    bear_2.show(window)


def main():
    # Initialize pygame settings - window, sushi events and music
    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("SushiBears")

    pygame.time.set_timer(SUSHI_CREATION, SUSHI_CREATION_INTERVAL_MILLISECONDS)
    pygame.mixer.music.load("Resources/game sound.wav")
    pygame.mixer.music.play(-1, 0.0)
    clock = pygame.time.Clock()

    # Our 2 Main characters
    bear_1 = bear.Bear(WINDOW_WIDTH, WINDOW_HEIGHT, 'bear_1')
    bear_2 = bear.Bear(WINDOW_WIDTH, WINDOW_HEIGHT, 'bear_2')

    is_running = True
    while is_running:
        clock.tick(FPS)
        draw_window(window, bear_1, bear_2)

        for current_sushi in sushi.Sushi.SUSHI_LIST:
            current_sushi.show(window)
            current_sushi.update(bear.Bear.BEAR_LIST)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False
                exit()

            if event.type == SUSHI_CREATION:
                sushi.Sushi(WINDOW_WIDTH, WINDOW_HEIGHT)

        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_LEFT] and bear_1.bear_rect.x > 0:
            bear_1.move('Left')
        if key_pressed[pygame.K_RIGHT] and bear_1.bear_rect.x < WINDOW_WIDTH - bear_1.BEAR_WIDTH:
            bear_1.move('Right')

        if key_pressed[pygame.K_a] and bear_2.bear_rect.x > 0:
            bear_2.move('Left')
        if key_pressed[pygame.K_d] and bear_2.bear_rect.x < WINDOW_WIDTH - bear_2.BEAR_WIDTH:
            bear_2.move('Right')

        check_for_winner(window, [bear_1, bear_2])

        pygame.display.update()


main()
