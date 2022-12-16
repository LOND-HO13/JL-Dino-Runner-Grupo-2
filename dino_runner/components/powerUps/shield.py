from dino_runner.components.powerUps.powe_up import PowerUp
from dino_runner.utils.constants import SHIELD, SHIELD_TYPE


class Shield(PowerUp):
    def __init__(self):
        super().__init__(SHIELD, SHIELD_TYPE) 

