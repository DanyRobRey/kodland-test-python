from game.components.power_ups.power_up import PowerUp
from game.utils.constants import THRUSTER

class Thruster(PowerUp):
    def __init__(self) -> None:
        self.name = 'Thruster'
        self.image = THRUSTER
        super().__init__(self.image)