import pygame.font
from pygame.sprite import Group

from ship import Ship

class Scoreboard:
    """A class to report scoring information"""

    def __init__(self, ai_game):
        """Intialize score keeping attributes"""
        self.ai_game = ai_game
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats

        #Font settings for scoring information
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        #prepare the initial score image
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()

    def prep_score(self):
        """Turn the score into a rendered image"""
        #round the number to the nearest 10
        rounded_score = round(self.stats.score, -1)
        score_str = "Score : {:,}".format(rounded_score)
        self.score_image = self.font.render(score_str, True,
                self.text_color, self.settings.bg_color)

        #Display the score at the top left of the screen
        self.score_rect = self.score_image.get_rect()
        self.score_rect.left = self.screen_rect.left + 20
        self.score_rect.top = 20

    def prep_high_score(self):
        high_score = round(self.stats.high_score, -1)
        high_score_str = "High Score : {:,}".format(high_score)
        self.high_score_image = self.font.render(high_score_str,
                True, self.text_color, self.settings.bg_color)

        # Display the high score at the top right of the screen
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.right = self.screen_rect.right - 20
        self.high_score_rect.top = self.score_rect.top

    def show_score(self):
        """Draw score, level and ships to the screen"""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.ships.draw(self.screen)

    def check_high_score(self):
        """Check to see if there's a new high score"""
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()

    def prep_level(self):
        """Turn the level into a rendered image"""
        level_str = "Level : " + str(self.stats.level)
        self.level_image = self.font.render(level_str, True, self.text_color,
                self.settings.bg_color)

        #Position the level below the score.
        self.level_rect = self.level_image.get_rect()
        self.level_rect.left = self.score_rect.left
        self.level_rect.top = self.score_rect.bottom + 10

    def prep_ships(self):
        """show how many ships are left"""
        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.ai_game)
            if self.stats.ships_left == 2:
                ship.rect.x = \
                    self.screen_rect.centerx - ship_number * ship.rect.width
            elif self.stats.ships_left == 3:
                ship.rect.x = \
                    self.screen_rect.centerx - ship_number * ship.rect.width \
                    + (ship.rect.width / 2)
            else:
                ship.rect.x = \
                    self.screen_rect.centerx - ship.rect.width / 2
            ship.rect.y = 10
            self.ships.add(ship)
