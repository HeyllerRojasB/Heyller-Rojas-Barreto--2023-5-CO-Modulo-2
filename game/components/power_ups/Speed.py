from game.components.power_ups.power_up import PowerUp
from game.utils.constants import RAY, SPEED_TYPE


class SpeedUp(PowerUp):
    def __init__(self):
        super().__init__(RAY,SPEED_TYPE)
        