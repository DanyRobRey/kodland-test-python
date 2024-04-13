from game.components.power_ups.shield import Shield
from game.components.power_ups.wrench import Wrench
from game.components.power_ups.thrusters import Thruster
from game.components.power_ups.score_bonus import ScoreBonus
from game.components.power_ups.cannon import Cannon

import random
class PowerUpHandler:
    INTERVAL_TIME = 300
    POWER_UPS = ['shield','wrench','thruster', 'score_bonus','cannon']

    def __init__(self) -> None:
        self.power_ups = []
        self.interval_time = 0

    def update(self, player):
        self.interval_time += 1
        if self.interval_time % self.INTERVAL_TIME == 0:
            self.add_power_up()
        for power_up in self.power_ups:
            power_up.update(player)
            if  not power_up.is_visible and not power_up.is_used:
                self.remove_power_up(power_up)
            if not power_up.is_activated and not power_up.is_visible and power_up.is_used:
                player.activate_power_up(power_up)
                power_up.is_activated = True
    
    
    def draw(self, screen):
        for power_up in self.power_ups:
            if power_up.is_visible:
                power_up.draw(screen)

    def add_power_up(self):
        random_power_up = random.choice(self.POWER_UPS)
        if random_power_up == self.POWER_UPS[0]:
            self.power_ups.append(Shield())
        elif random_power_up == self.POWER_UPS[1]:
            self.power_ups.append(Wrench())
        elif random_power_up == self.POWER_UPS[2]:
            self.power_ups.append(Thruster())
        elif random_power_up == self.POWER_UPS[3]:
            self.power_ups.append(ScoreBonus())
        elif random_power_up == self.POWER_UPS[4]:
            self.power_ups.append(Cannon())

    def remove_power_up(self, power_up):
        self.power_ups.remove(power_up)

    def reset(self):
        self.power_ups = []
        self.interval_time = 0

