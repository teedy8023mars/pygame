import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    def __init__(self, ai_game):
        #init alien position
        super().__init__()
        self.screen = ai_game.screen
        #load alien image
        self.image = pygame.image.load('./pics/aliens.png')
        self.rect = self.image.get_rect()
        #each one at the top left initially
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        #store precise initial position
        self.x = float(self.rect.x)
