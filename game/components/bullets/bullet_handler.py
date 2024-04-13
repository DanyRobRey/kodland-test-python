from game.utils.constants import BULLET_ENEMY_TYPE, BULLET_ALLY_TYPE, BULLET_ALLY_CANNON_TYPE
from game.components.bullets.bullet_enemy import BulletEnemy
from game.components.bullets.bullet_ally import BulletAlly
from game.components.bullets.bullet_ally_cannon import BulletAllyCannon

class BulletHandler:
    def __init__(self) -> None:
        self.bullets = []

    def update(self, player, enemy_handler):
        for bullet in self.bullets:
            if not bullet.is_alive:
                self.remove_bullet(bullet)
            if type(bullet) == BulletEnemy:
                bullet.update(player)
            elif type(bullet) == BulletAlly:
                bullet.update(player)
            elif type(bullet) == BulletAllyCannon:
                bullet.update(player)

    def draw(self, screen):
        for bullet in self.bullets:
            bullet.draw(screen)

    def add_bullet(self, type, center):
        if type == BULLET_ENEMY_TYPE:
            self.bullets.append(BulletEnemy(center))
        elif type == BULLET_ALLY_TYPE:
            self.bullets.append(BulletAlly(center))
        elif type == BULLET_ALLY_CANNON_TYPE:
            self.bullets.append(BulletAllyCannon(center))

    def remove_bullet(self, bullet):
        self.bullets.remove(bullet)

    def reset(self):
        self.bullets = []