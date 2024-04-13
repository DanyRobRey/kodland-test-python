import pygame
from game.components.bullets.bullet import Bullet
from game.utils.constants import BULLET

class BulletAlly(Bullet):

    WIDTH = 30
    HEIGHT = 40
    SPEED = 40

    def __init__(self, center):
        self.image = BULLET
        self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGHT))
        super().__init__(self.image, center)

    def update(self, player):
        self.rect.y -= self.SPEED
        super().update(player)

