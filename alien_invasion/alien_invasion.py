import sys
import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien

class AlienInvasion:
    """Overall class to manage game and assets and behavior"""

    def __init__(self):
        """Initialize the game, and create game resources"""
        pygame.init()
        self.settings = Settings()

        #Create the screen using the dimensions in the tuples
        self.screen = pygame.display.set_mode((self.settings.screen_width,
            self.settings.screen_height))

        """Run in full screen
        self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        """

        #Screen title
        pygame.display.set_caption("Alien Invasion")

        #Create a ship and pass the current instance of AlienInvasion to it
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()


    def run_game(self):
        """Start the main loop for the game"""
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()

            self._update_screen()

    #Helper Method
    def _check_events(self):
        #Watch for keyboard and mouse events
        for event in pygame.event.get():
            #exit the game by clicking the x
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    #Helper Methods
    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            # Move the ship to the right
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            # Move the ship to the left
            self.ship.moving_left = True
        elif event.key == pygame.K_l:
            # Move the ship to the right
            self.ship.moving_right = True
        elif event.key == pygame.K_h:
            # Move the ship to the left
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            # quit the game if q is pressed
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            # Move the ship to the right
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            # Move the ship to the left
            self.ship.moving_left = False
        elif event.key == pygame.K_l:
            # Move the ship to the right
            self.ship.moving_right = False
        elif event.key == pygame.K_h:
            # Move the ship to the left
            self.ship.moving_left = False

    def _fire_bullet(self):
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """Update the postion of bullets and get rid of old bullets"""
        #update bullet positions
        self.bullets.update()

        # Get rid of bullets that have dissapeared
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

    def _create_fleet(self):
        """Create the fleet of aliens."""
        #make an alien
        alien = Alien(self)
        self.aliens.add(alien)

    def _update_screen(self):
        #Redraw the screen during each pass through the loop.
        #fill in the screen background
        self.screen.fill(self.settings.bg_color)
        #Draw the ship
        self.ship.blitme()

        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        # draw the alien , draw takes the surface on which to draw the alien
        self.aliens.draw(self.screen)

        # Make the most recently drawn screen visible.
        pygame.display.flip()


# run game
if __name__ == '__main__':
    #Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()
