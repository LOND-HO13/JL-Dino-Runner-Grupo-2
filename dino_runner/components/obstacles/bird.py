from random import randint
from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import BIRD


class Bird(Obstacle):

    def __init__(self, image):
        self.bird = BIRD[0]
        super().__init__(BIRD[0])
        self.rect.y = randint(200,300)
        self.index = 0
        
    
    def draw(self, screen):
        if self.index >= 9:
            self.index = 0
        screen.blit(BIRD[self.index//5], self.rect)
        self.index += 1
        
        


