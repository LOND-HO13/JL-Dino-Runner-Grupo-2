from random import randint
import pygame
from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.components.obstacles.obstacle_manager import ObstacleManager
from dino_runner.components.powerUps.hammer import Hammer
from dino_runner.components.powerUps.heart import Heart
from dino_runner.components.powerUps.powe_up import PowerUp
from dino_runner.components.powerUps.shield import Shield
from dino_runner.utils.constants import HEART_TYPE, SHIELD_TYPE, SOUND_POWERUP, SOUND_VOLUMEN



class PowerUpManager:
    def __init__(self):
        self.power_ups: list[PowerUp] = []
        
        self.when_appears = 0
        
        
    def generate_power_up(self, score):
        if not self.power_ups and self.when_appears == score:
            ran = randint(0,2)
            if ran == 0:
                self.power_ups.append(Shield())
            elif ran == 1:
                self.power_ups.append(Hammer())
            else:
                self.power_ups.append(Heart()) 
            self.when_appears += randint(200, 300)
    
    def update(self, game_speed, score, player):
        self.generate_power_up(score)
        for power_up in self.power_ups: 
            power_up.update(game_speed, self.power_ups)
            if  power_up.type == SHIELD_TYPE:
                if power_up.rect.colliderect(player.rect):
                    power_up.start_time = pygame.time.get_ticks()
                    player.on_pick_power_up(power_up)
                    self.power_ups.remove(power_up)
                    pygame.mixer.Sound.play(SOUND_POWERUP)
                    pygame.mixer.Sound.set_volume( SOUND_POWERUP,SOUND_VOLUMEN)
            elif power_up.type == HEART_TYPE:
                if power_up.rect.colliderect(player.rect):
                    self.power_ups.remove(power_up)
                    player.lifes += 1
                    pygame.mixer.Sound.play(SOUND_POWERUP)
                    pygame.mixer.Sound.set_volume( SOUND_POWERUP,SOUND_VOLUMEN)
            else:
                if power_up.rect.colliderect(player.rect):
                    power_up.start_time = pygame.time.get_ticks()
                    player.on_pick_power_up(power_up)
                    self.power_ups.remove(power_up)
                    pygame.mixer.Sound.play(SOUND_POWERUP)
                    pygame.mixer.Sound.set_volume( SOUND_POWERUP,SOUND_VOLUMEN)
                    
    def draw(self, screen):
        for power_up in self.power_ups:
            power_up.draw(screen)
        
    def reset_power_ups(self):
        self.power_ups = []
        self.when_appears = randint(200, 300)