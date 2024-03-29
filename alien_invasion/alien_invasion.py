import sys
from time import sleep
import pygame
import json
import pygame.font

from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard

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

        #Create an instance to store game statistics,
        # and create a scoreboard
        self.stats = GameStats(self)
        self.sb = Scoreboard(self)

        #Create a ship and pass the current instance of AlienInvasion to it
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()

        # Make the play button
        self.play_button = Button(self, "Play")


    def run_game(self):
        """Start the main loop for the game"""
        while True:
            self._check_events()

            if self.stats.game_active == 1:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()

            self._update_screen()

    #Helper Method
    def _check_events(self):
        #Watch for keyboard and mouse events
        for event in pygame.event.get():
            #exit the game by clicking the x
            if event.type == pygame.QUIT:
                with open(self.settings.filename, 'w') as f:
                    json.dump(self.stats.high_score, f)
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

    def _check_play_button(self, mouse_pos):
        """Start a new game when the player clicks Play."""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and self.stats.game_active == 0:
            # Reset the game settings.
            self.settings.initialze_dynamic_settings()
            self.sb.prep_score()
            self.sb.prep_ships()
            self._start_game()

    def _start_game(self):
        self.stats.reset_stats()
        self.stats.game_active = 1

        #Get rid of any remaining aliens and bullets.
        self.aliens.empty()
        self.bullets.empty()

        #Create a new fleet and center the ship.
        self._create_fleet()
        self.ship.center_ship()

        #hide the mouse cursor
        pygame.mouse.set_visible(False)

    def _pause_game(self):
        if self.stats.game_active == 2:
            self.stats.game_active = 1
        else:
            self.stats.game_active = 2
            self.pause_str = "Paused"
            self.font = pygame.font.SysFont(None,48)
            self.pause_image = self.font.render(self.pause_str, True, (30, 30, 30),
                    self.settings.bg_color)

            self.pause_rect = self.pause_image.get_rect()
            self.pause_rect.centerx = self.screen.get_rect().centerx
            self.pause_rect.centery = self.screen.get_rect().centery

            self.screen.fill(self.settings.bg_color)

            self.screen.blit(self.pause_image, self.pause_rect)

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
            with open(self.settings.filename, 'w') as f:
                json.dump(self.stats.high_score, f)
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        elif event.key == pygame.K_RETURN:
            self._start_game()
        elif event.key == pygame.K_p:
            self._pause_game()

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

        self._check_bullet_alien_collision()


    def _check_bullet_alien_collision(self):
        """Respond to bullet-alien collisions"""
        # Remove any bullets and aliens that have collided

        # Check for any bullets that have hit aliens.
        #   If so, get rid of the bullet and the alien
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens,
                True, True)

        if collisions:
            for aliens in collisions.values():
                self.stats.score += \
                self.settings.alien_points * len(aliens)
            self.sb.prep_score()
            self.sb.check_high_score()
            self.sb.prep_level()

        if not self.aliens:
            #Destroy existing bullets and create new fleet.
            self.bullets.empty()
            self._create_fleet()
            self.settings.increase_speed()

            # Increase level
            self.stats.level += 1
            self.sb.prep_level()


    def _create_fleet(self):
        """Create the fleet of aliens."""
        #Create an alien and find the number of alien in a row.
        # spacing between each alien is equal to one alien width
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size

        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens = available_space_x // (2 * alien_width)

        #Determine the number of rows of aliens that fit on the screen.
        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_height -
                (3 * alien_height) - ship_height)
        number_rows = available_space_y // (2 * alien_height)

        # Create the first row of aliens
        for row_number in range(number_rows):
            for alien_number in range(number_aliens):
                self._create_alien(alien_number, row_number)


    def _create_alien(self, alien_number, row_number):
            # Create and alien and place it in the row
            alien = Alien(self)
            alien_width, alien_height = alien.rect.size
            alien.x = alien_width + 2 * alien_width * alien_number
            alien.rect.x = alien.x
            alien.rect.y = alien.rect.height + 2 * alien.rect.height *\
                    row_number
            self.aliens.add(alien)

    def _update_aliens(self):
        """Update the positions of all aliens in the fleet"""
        #Check if the fleet is at an edge, then update the positions of
        # all aliens in the fleet
        self._check_fleet_edges()
        self.aliens.update()

        # Look for alien-ship collisions.
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

        # Looking for aliens hitting the bottom of the screen
        self._check_aliens_bottom()

    def _check_fleet_edges(self):
        """Respond appropriately if any aliens hae reached an edge."""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """Drop the entire fleet and change the fleet's direction."""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _check_aliens_bottom(self):
        """Check if any aliens have reached the bottom of the screen"""
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                # Treat this the same as the ship got hit
                self._ship_hit()
                break

    def _ship_hit(self):
        """Respond to the ship being hit by an alien"""
        if self.stats.ships_left > 1:
            # Decrement ships left, and update scoreboard
            self.stats.ships_left -= 1
            self.sb.prep_ships()

            # Get rid of any remaining aliens and bullets.
            self.aliens.empty()
            self.bullets.empty()

            # Create a new fleet and center the ship()
            self._create_fleet()
            self.ship.center_ship()

            # Pause
            sleep(0.5)
        else:
            self.stats.game_active = 0
            pygame.mouse.set_visible(True)

    def _update_screen(self):
        #Redraw the screen during each pass through the loop.
        #fill in the screen background
        self.screen.fill(self.settings.bg_color)
            #Draw the ship
        if self.stats.game_active == 1:
            self.ship.blitme()

            for bullet in self.bullets.sprites():
                bullet.draw_bullet()

            # draw the alien , draw takes the surface on which to draw the alien
            self.aliens.draw(self.screen)

            #Draw the score information
            self.sb.show_score()

        # Draw the play button if the game is inactive
        if self.stats.game_active == 0:
            self.play_button.draw_button()

        # Make the most recently drawn screen visible.
        pygame.display.flip()


# run game
if __name__ == '__main__':
    #Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()
