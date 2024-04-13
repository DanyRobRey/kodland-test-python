from game.components.power_ups.power_up import PowerUp
from game.utils.constants import WRENCH

class Wrench(PowerUp):
    def __init__(self) -> None:
        self.name = 'Wrench'
        self.image = WRENCH
        super().__init__(self.image)