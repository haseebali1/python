import pygame

class Ship:
    """ A class to manage the ship."""

    #ai_game is current instance of the AlienInvasion class
    def __init__(self, ai_game):
        """Initialize the ship and set its starting position"""

        #assign ship screen attribute to easily access it
        self.screen = ai_game.screen
        #get the screen rect to place ship in correct location
        self.screen_rect = ai_game.screen.get_rect()

        #Load the ship image and get its rect.
        self.image = pygame.image.load('img/ship.bmp')
        self.rect = self.image.get_rect()

        # start each new ship at the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom

        self.moving_right = False

    def update(self):
        """update the ship's position based on the movement flag"""
        if self.moving_right:
            self.rect.x += 1

    def blitme(self):
        """Draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)
