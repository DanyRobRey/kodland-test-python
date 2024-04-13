import math
import pygame
from game.components.enemies.enemy import Enemy
from game.utils.constants import ENEMY_OVNI, SCREEN_WIDTH, SCREEN_HEIGHT

class Ovni(Enemy):

    WIDTH = 40
    HEIGHT = 60
    SPEED_X = 2
    SPEED_Y = 2
    LIVES = 2

    def __init__(self):
        self.image = ENEMY_OVNI
        self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGHT))
        super().__init__(self.image, self.LIVES)

    # def update(self): Add logic for different movements
    #     super().update()
        