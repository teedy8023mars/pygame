from random import randint


class Settings:
    def __init__(self):
        self.screen_width, self.screen_height = (1100, 700)
        self.bg_color = (29, 37, 44)
        self.ship_speed = 6
        #setting for bullet
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (244, 214, 60)
        self.bullet_allowed = 30  #bullet limit
        #stars
        self.number_of_stars = 200
