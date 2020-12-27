from random import randint
from pygame import *
import pygame


class Settings:
    def __init__(self):
        self.screen_width, self.screen_height = (1100, 700)
        self.bg_color = (29, 37, 44)
        self.ship_speed = 10
        self.ship_limit = 3
        # setting for bullet
        self.bullet_speed = 10
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (244, 214, 60)
        self.bullet_allowed = 30  # bullet limit
        # stars
        self.number_of_stars = 200
        self.alien_speed = 3
        self.fleet_drop_speed = 10
        # 1 means right -1 means left
        self.fleet_dir = 1
        # FPS
        self.clock = pygame.time.Clock()
