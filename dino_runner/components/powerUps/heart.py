from dino_runner.components.powerUps.powe_up import PowerUp
from dino_runner.utils.constants import HEART, HEART_TYPE


class Heart(PowerUp):
      def __init__(self):
        super().__init__(HEART, HEART_TYPE) 