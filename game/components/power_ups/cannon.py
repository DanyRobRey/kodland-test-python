from game.components.power_ups.power_up import PowerUp
from game.utils.constants import SPACESHIP_CANNON

class Cannon(PowerUp):
    def __init__(self) -> None:
        self.name = 'Cannon'
        self.image = SPACESHIP_CANNON
        super().__init__(self.image)