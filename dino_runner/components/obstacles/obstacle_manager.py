import pygame
from random import randint
from dino_runner.components.obstacles.cactus import Cactus, CactusLarge
from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import LARGE_CACTUS, SMALL_CACTUS


class ObstacleManager:
    
    def __init__(self):
        self.obstacles: list[Obstacle]=[]
        
        
    def update(self, game):
        
        if len(self.obstacles) == 0:
            ran= randint(0,1)
            if ran ==0:
                self.obstacles.append(Cactus(SMALL_CACTUS))
            else:
                self.obstacles.append(CactusLarge(LARGE_CACTUS))
            
            
        # if not self.obstacles:
        #     pass
        
        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if  obstacle.rect.colliderect(game.player.rect):
                pygame.time.delay(500)
                game.playing = False
    
    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)
        
        