import pygame

class Hero:
    def __init__(self, screen):
        self.image = pygame.image.load('img/hero.png')
        self.rect = self.image.get_rect()
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.rect.bottom = self.screen_rect.bottom
        self.rect.center = self.screen_rect.center

    def output_hero(self):
        self.screen.blit(self.image, self.rect)