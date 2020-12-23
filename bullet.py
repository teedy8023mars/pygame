import pygame
from pygame.sprite import Sprite
import settings


class Bullet(Sprite):
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color
        #(0,0) frame a rect to contain a bullet
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width,
                                self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop
        #储存用小数表示的子弹位置
        self.y = float(self.rect.y)

    def update(self):
        #move bullet up
        self.y -= self.settings.bullet_speed
        #update the position of bullet
        self.rect.y = self.y

    def draw_bullet(self):
        #draw bullet on the screen
        pygame.draw.rect(self.screen, self.color, self.rect)
