import pygame
from random import randint
from dino_runner.components.obstacles.bird import Bird
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import LARGE_CACTUS, SMALL_CACTUS, BIRD

SMALL_CACTUS_Y_POS = 325
LARGE_CACTUS_Y_POS = 300

class ObstacleManager:
    
    def __init__(self):
        self.obstacles: list[Obstacle]=[]
        
        
    def update(self, game):
        
        if len(self.obstacles) == 0:
            ran= randint(0,2)
            if ran ==0:
                self.obstacles.append(Cactus(SMALL_CACTUS, SMALL_CACTUS_Y_POS))
            elif ran ==1:
                self.obstacles.append(Cactus(LARGE_CACTUS, LARGE_CACTUS_Y_POS))
            else: 
                self.obstacles.append(Bird(BIRD))
            

        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if  obstacle.rect.colliderect(game.player.rect):
                pygame.time.delay(500)
                game.playing = False
                game.death_count += 1
    
    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)
        
    def reset_obstacules(self):
        self.obstacles = []