import pygame
from pygame.sprite import Sprite
from settings import Settings


class Alien(Sprite):
    def __init__(self, ai_game):
        # init alien position
        super().__init__()
        self.setting = ai_game.settings
        self.screen = ai_game.screen
        # load alien image
        self.image = pygame.image.load('./pics/aliens.png')
        self.rect = self.image.get_rect()
        # each one at the top left initially
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        # store precise initial position
        self.x = float(self.rect.x)

    def update(self):
        self.x += (self.setting.alien_speed * self.setting.fleet_dir)
        self.rect.x = self.x

    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True
