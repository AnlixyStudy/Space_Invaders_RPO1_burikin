import pygame
import sys
from Hero import Hero

def start_game():
    W = 600  # ширина экрана
    H = 900
    pygame.init()
    sc = pygame.display.set_mode((W, H))
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((W,H))
    pygame.display.set_caption('Game')
    bg = (255,255,255)
    BLUE = (0, 70, 225)

    x = W // 2
    y = H // 2
    STOP = "stop"
    motion = STOP
    RIGHT = "to the right"
    LEFT = "to the left"

    hero = Hero(screen)

    flag = True
    while flag:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    hero.rect.centerx += -10
                elif event.key == pygame.K_RIGHT:
                    hero.rect.centerx += 10
            elif event.type == pygame.KEYUP:
                if event.key in [pygame.K_LEFT,
                         pygame.K_RIGHT]:
                    motion = STOP
        pygame.display.flip()
        screen.fill(bg)
        hero.output_hero()
        pygame.display.update()
        clock.tick(60)

start_game()