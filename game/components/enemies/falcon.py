import pygame
from game.components.enemies.enemy import Enemy
from game.utils.constants import ENEMY_FALCON

class Falcon(Enemy):

    WIDTH = 80
    HEIGHT = 60
    SPEED_X = 2
    SPEED_Y = 2
    LIVES = 5

    def __init__(self):
        self.image = ENEMY_FALCON
        self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGHT))
        super().__init__(self.image, self.LIVES)