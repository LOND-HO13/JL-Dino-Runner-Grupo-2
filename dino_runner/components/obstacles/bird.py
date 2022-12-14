from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import BIRD
from random import randint

class Bird(Obstacle):
    
    def __init__(self):
        self.image = BIRD[0]
        self.resect_rect()
        self.step = 0
        self.rect.y = 100
            
    def resect_rect(self, y_pos=None):
        self.rect = self.image.get_rect()
        self.rect.x = self.X_POS 
        self.rect.y = y_pos or self.Y_POS
    
    def update(self):
        pass
    
    def fly(self):
        self.image = BIRD[self.step // 5]
        self.resect_rect()
        self.step += 1
    
    def draw(self, screen):
        pass

