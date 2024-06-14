import sys

import pygame

from settings import Settings
from src.ship import Ship


class AlienInvasion:
    """ Overall class to manage game assets and behavior"""

    def __init__(self):
        """ Initialize the game, and create game resources"""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        # notice the display.set_mode is what initializes the screen
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)

    def run_game(self):
        """start the main loop"""
        while True:
            # watch for keyboard and mouse events
            self._check_events()
            self.ship.update()
            self._update_screen()
            self.clock.tick(60)

    def _update_screen(self):
        # redraw the screen during each pass
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        # flip to the most recent drawn screen
        pygame.display.flip()

    def _check_events(self):
        for event in pygame.event.get():  # reports all events since last time this func was called
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:  # arrow key pressed
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = True
                if event.key == pygame.K_LEFT:
                    self.ship.moving_left = True
                if event.key == pygame.K_UP:
                    self.ship.moving_up = True
                if event.key == pygame.K_DOWN:
                    self.ship.moving_down = True

            elif event.type == pygame.KEYUP:    # arrow key released
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = False
                if event.key == pygame.K_LEFT:
                    self.ship.moving_left = False
                if event.key == pygame.K_UP:
                    self.ship.moving_up = False
                if event.key == pygame.K_DOWN:
                    self.ship.moving_down = False


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
