import sys
import pygame

from settings import Settings
from ship import Ship

class AlienInvasion:
    """Overall class to manage game and assets and behavior"""

    def __init__(self):
        """Initialize the game, and create game resources"""
        pygame.init()
        self.settings = Settings()

        #Create the screen using the dimensions in the tuples
        self.screen = pygame.display.set_mode((self.settings.screen_width,
            self.settings.screen_height))
        #Screen title
        pygame.display.set_caption("Alien Invasion")

        #Create a ship and pass the current instance of AlienInvasion to it
        self.ship = Ship(self)


    def run_game(self):
        """Start the main loop for the game"""
        while True:
            #Watch for keyboard and mouse events
            for event in pygame.event.get():
                #exit the game by clicking the x
                if event.type == pygame.QUIT:
                    sys.exit()

            #Redraw the screen during each pass through the loop.
            #fill in the screen background
            self.screen.fill(self.settings.bg_color)
            #Draw the ship
            self.ship.blitme()

            # Make the most recently drawn screen visible.
            pygame.display.flip()

if __name__ == '__main__':
    #Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()