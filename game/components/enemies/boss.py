import pygame
from game.components.enemies.enemy import Enemy
from game.utils.constants import BOSS

class Boss(Enemy):

    WIDTH = 500
    HEIGHT = 250
    SPEED_X = 2
    SPEED_Y = 2

    def __init__(self, lifes):
        self.image = BOSS
        self.energy = 100
        self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGHT))
        super().__init__(self.image, lifes)