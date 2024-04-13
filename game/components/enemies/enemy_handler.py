from game.components.enemies.ship import Ship
from game.components.enemies.ovni import Ovni
from game.components.enemies.betrayer import Betrayer
from game.components.enemies.marauder import Marauder
from game.components.enemies.falcon import Falcon
from game.components.enemies.lance import Lance
from game.components.enemies.orbit import Orbit
from game.components.enemies.pylon import Pylon
from game.components.enemies.boss import Boss
import random

class EnemyHandler:
    ENEMY_TYPES = ['ship',
                   'ovni',
                   'betrayer',
                   'marauder',
                   'falcon',
                   'lance',
                   'orbit',
                   'pylon']
    def __init__(self):
        self.enemies = []
        self.enemies_destroyed = 0
        self.bonus = False 
        self.is_reset = False
        self.previous_life = False

    def update(self, bullet_handler, last_wave):
        if last_wave and not self.is_reset:
            if self.previous_life:
                self.previous_life = self.enemies[0].lifes
            self.enemies = []
            self.is_reset = True
        if len(self.enemies) == 0:
            self.add_enemy(last_wave)
        for enemy in self.enemies:
            enemy.update(bullet_handler)
            if not enemy.is_visible or not enemy.is_alive:
                self.remove_enemy(enemy)
            if not enemy.is_alive:
                if self.bonus:
                    self.enemies_destroyed += 2
                else:
                    self.enemies_destroyed += 1

    def draw(self, screen):
        for enemy in self.enemies:
            enemy.draw(screen)

    def add_enemy(self, last_wave):
        if last_wave:
            random_enemy = 'boss'
            if not self.previous_life:
                self.previous_life = 20
            new_enemy = Boss(self.previous_life)
            c = 0
            while c < random.randint(50, 150):
                c += 1
            c = 0
            self.enemies.append(new_enemy)
        else:
            random_enemy = random.choice(self.ENEMY_TYPES)
            for _ in range(5):
                if random_enemy == 'ship':
                    new_enemy = Ship()
                elif random_enemy == 'ovni':
                    new_enemy = Ovni()
                elif random_enemy == 'betrayer':
                    new_enemy = Betrayer()
                elif random_enemy == 'marauder':
                    new_enemy = Marauder()
                elif random_enemy == 'falcon':
                    new_enemy = Falcon()
                elif random_enemy == 'lance':
                    new_enemy = Lance()
                elif random_enemy == 'orbit':
                    new_enemy = Orbit()
                elif random_enemy == 'pylon':
                    new_enemy = Pylon()

            
                self.enemies.append(new_enemy)

    def remove_enemy(self, enemy):
        self.enemies.remove(enemy)

    def reset(self):
        self.enemies = []
        self.enemies_destroyed = 0 


    