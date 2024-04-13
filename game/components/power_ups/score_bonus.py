from game.components.power_ups.power_up import PowerUp
from game.utils.constants import SCORE_BONUS

class ScoreBonus(PowerUp):
    def __init__(self) -> None:
        self.name = 'Score Bonus'
        self.image = SCORE_BONUS
        super().__init__(self.image)