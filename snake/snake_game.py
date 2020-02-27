import sys
import pygame

from settings import Settings

class SnakeGame:
    """Overall class to manage game and assets and behavior"""

    def __init__(self):
        """Initialize the game, and create game resources"""

        pygame.init()
        self.settings = Settings()

        #Create the screen using the dimensions in the tuples
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))

        #Screen title
        pygame.display.set_caption("Snake Game")

    def run_game(self):
        """Start the main loop for the game"""
        while True:
            self._check_events()

            self._update_screen()

    #Helper Method
    def _check_events(self):
        #watch for keyboard and mouse events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)

    def _check_keydown_events(self, event):
        if event.key == pygame.K_q:
            sys.exit()


    def _update_screen(self):
        #Redraw the screen during each pass through the loop
        #fill in the screen background

        self.screen.fill(self.settings.bg_color)

        pygame.display.flip()


if __name__ == '__main__':
    #make a game instance and run the game
    sg = SnakeGame()
    sg.run_game()

