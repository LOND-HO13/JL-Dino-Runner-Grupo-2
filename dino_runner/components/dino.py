import pygame
from pygame.sprite import Sprite
from dino_runner.components.draw_message import draw_message
from dino_runner.utils.constants import (
    DEFAULT_TYPE,
    DINO_DEAD, 
    DUCKING_SHIELD,
    HEART_TYPE, 
    JUMPING_SHIELD,
#    MUSIC_JUMP, 
    RUNNING, 
    JUMPING, 
    DUCKING, 
    RUNNING_SHIELD,
    SCREEN_WIDTH, 
    SHIELD_TYPE
    )

jumping_action = "jumping"
running_action = "runing"
duck_action = "ducking"

DUCK_IMG = {
    DEFAULT_TYPE: DUCKING,
    SHIELD_TYPE: DUCKING_SHIELD,
    HEART_TYPE: DUCKING
}

RUN_IMG = {
    DEFAULT_TYPE: RUNNING,
    SHIELD_TYPE: RUNNING_SHIELD,
    HEART_TYPE: RUNNING
}

JUMP_IMG = {
    DEFAULT_TYPE: JUMPING,
    SHIELD_TYPE: JUMPING_SHIELD,
    HEART_TYPE: JUMPING
}

class Dinosaur(Sprite):
    Y_POS = 310
    X_POS = 80
    Y_POS_DUCK = 340
    JUMP_VELOCITY = 8.5
    
    def __init__(self):
        self.type = DEFAULT_TYPE
        self.image = RUN_IMG[self.type][0]
        self.resect_rect()
        self.jump_velocity = self.JUMP_VELOCITY
        self.step = 0
        self.action = running_action
        self.has_power_up = False
        self.power_up_time_up = 0
        self.lifes = 5
        #self.sound_jump = pygame.mixer.Sound(MUSIC_JUMP)
              
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
        self.image = RUN_IMG[self.type][self.step // 5]
        self.resect_rect()
        self.step += 1
        
    def jump(self):
        self.image = JUMP_IMG[self.type]
        #self.play()
        y_pos = self.rect.y - self.jump_velocity * 4
        self.resect_rect(y_pos=y_pos)
        self.jump_velocity -= 0.8
        if self.jump_velocity < -self.JUMP_VELOCITY:
            self.resect_rect()
            self.jump_velocity = self.JUMP_VELOCITY
            self.action = running_action
        
    def duck(self):
        self.image = DUCK_IMG[self.type][self.step // 5]
        self.resect_rect(y_pos=self.Y_POS_DUCK)
        self.step +=1
    
    def draw(self, screen):
        screen.blit(self.image, (self.rect.x , self.rect.y))
        
    def on_pick_power_up(self, power_up):
        self.has_power_up = True
        self.power_up_time_up = power_up.start_time + (power_up.duration * 1000)
        self.type = power_up.type
    
    def draw_active_power_uo(self, screen):
        if self.has_power_up:
            left_time = round((self.power_up_time_up - pygame.time.get_ticks()) / 1000, 2)
            if left_time >= 0:
                draw_message(
                   f"{self.type.capitalize()} enabled for {left_time} seconds.",
                   screen,
                   (0,0,0),
                   pos_x_center= 520,
                   pos_y_center = 40
                )
            else:
                self.type = DEFAULT_TYPE
                self.has_power_up = False
    
    def on_dino_dead(self):
        self.image = DINO_DEAD
        
    def draw_life(self,screen):
        draw_message(
            f"your lifes: {self.lifes}", 
            screen, 
            (0,0,0), 
            pos_x_center = 80, 
            pos_y_center = 40
            )