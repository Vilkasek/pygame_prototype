import pygame
import sys

pygame.init()

# Window and time stuff
screen_size = (1260, 720)

pygame.display.set_caption("Prototype")
screen = pygame.display.set_mode(screen_size)

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((84, 5, 163))

    clock.tick(60)
    pygame.display.update()
