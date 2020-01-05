import sys
import pygame

from settings import Settings
from character import Character

class MainGame:

    def __init__(self):
        pygame.init()

        self.settings = Settings()

        self.screen = pygame.display.set_mode(
                ( self.settings.screen_width, self.settings.screen_height ))
        pygame.display.set_caption("Main")

        self.character = Character(self)

    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()


            self.screen.fill(self.settings.bg_color)
            self.character.blitme()
            pygame.display.flip()



if __name__ == '__main__':
    main_game = MainGame()
    main_game.run_game()
