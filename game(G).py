import pygame
import random

pygame.init()

WIDTH, HEIGHT = 800, 600
FPS = 60

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Starship Game")

score = 0
difficulty_level = 1
meteor_speed = 5
diagonal_meteor_speed = 5
shooting_star_speed = 5

clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if score > 0 and score % 50 == 0:
        difficulty_level += 1
        meteor_speed += 2
        diagonal_meteor_speed += 1
        shooting_star_speed += 1

    meteors_evaded = 0
    diagonal_meteors_evaded = 0
    shooting_stars_evaded = 0
    meteors_destroyed = 0
    diagonal_meteors_destroyed = 0
    shooting_stars_destroyed = 0

    score = (
        meteors_evaded + diagonal_meteors_evaded + shooting_stars_evaded +
        meteors_destroyed + diagonal_meteors_destroyed + shooting_stars_destroyed
    )

    font = pygame.font.Font(None, 36)
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (WIDTH - 150, 20))

    pygame.display.flip()

    clock.tick(FPS)

pygame.quit()
