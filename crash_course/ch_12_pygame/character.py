import pygame

class Character:

    def __init__(self,mgame):
        self.screen = mgame.screen
        self.screen_rect = mgame.screen.get_rect()

        self.image = pygame.image.load('img/ship.bmp')
        self.rect = self.image.get_rect()

        self.rect.center = self.screen_rect.center

    def blitme(self):
        self.screen.blit(self.image, self.rect)
