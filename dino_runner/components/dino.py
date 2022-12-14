import pygame
from pygame.sprite import Sprite
from dino_runner.utils.constants import RUNNING, JUMPING, DUCKING

jumping_action = "jumping"
running_action = "runing"
duck_action = "ducking"

class Dinosaur(Sprite):
    Y_POS = 310
    X_POS = 80
    Y_POS_DUCK = 340
    JUMP_VELOCITY = 8.5
    
    def __init__(self):
        self.image = RUNNING[0]
        self.resect_rect()
        self.jump_velocity = self.JUMP_VELOCITY
        self.step = 0
        self.action = running_action
              
    def resect_rect(self, y_pos=None):
        self.rect = self.image.get_rect()
        self.rect.x = self.X_POS 
        self.rect.y = y_pos or self.Y_POS
    
    def update(self, user_input):
        if self.action == running_action:  
            self.run()
            
        elif self.action == jumping_action:
            self.jump()
        
        elif self.action == duck_action:
            self.duck()
            
        if self.action != jumping_action:
            if user_input[pygame.K_UP]:
                self.action = jumping_action
            else:
                 if user_input[pygame.K_DOWN]:
                     self.action = duck_action
                 else:
                    self.action = running_action
        
        if self.step >= 9:
            self.step = 0
            
    def run(self):
        self.image = RUNNING[self.step // 5]
        self.resect_rect()
        self.step += 1
        
    def jump(self):
        self.image = JUMPING
        y_pos = self.rect.y - self.jump_velocity * 4
        self.resect_rect(y_pos=y_pos)
        self.jump_velocity -= 0.8
        if self.jump_velocity < -self.JUMP_VELOCITY:
            self.resect_rect()
            self.jump_velocity = self.JUMP_VELOCITY
            self.action = running_action
        
    def duck(self):
        self.image = DUCKING[self.step // 5]
        self.resect_rect(y_pos=self.Y_POS_DUCK)
        self.step +=1
    
    def draw(self, screen):
        screen.blit(self.image, (self.rect.x , self.rect.y))