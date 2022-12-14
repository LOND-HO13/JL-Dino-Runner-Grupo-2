
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import SMALL_CACTUS

class ObstacleManager:
    
    def __init__(self):
        self.obstacles = list[Obstacle]=[]
        
    def update(self, game_speed):
        
        if len(self.obstacles) == 0:
            self.obstacles.append(Cactus(SMALL_CACTUS))
            
        # if not self.obstacles:
        #     pass
        
        for obstacle in self.obstacles:
            obstacle.update(game_speed, self.obstacles)
            # if  obstacle.rect.colliderect(Game.player.rect):
            #     pygame.time.delay(1000)
            #     game.playing = False
    
    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)
        
        