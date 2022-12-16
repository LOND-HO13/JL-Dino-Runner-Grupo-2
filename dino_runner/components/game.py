import pygame
from dino_runner.components.cloud import Cloud
from dino_runner.components.dino import Dinosaur
from dino_runner.components.obstacles.obstacle_manager import ObstacleManager
from dino_runner.components.obstacles.score import Score
from dino_runner.components.powerUps.power_up_manager import PowerUpManager

from dino_runner.utils.constants import BG, BOTON_RESET, DINO_START, FONT_STYLE, GAME_OVER, HAMMER_TYPE, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, SHIELD_TYPE,  TITLE, FPS


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        
        self.playing = False
        self.game_speed = 20
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        
        self.cloud = Cloud()
        self.player = Dinosaur()
        self.player.lifes = 5
        self.obstacle_manager = ObstacleManager()
        self.power_up_manager = PowerUpManager()
        self.score = Score()
        self.death_count = 0
        self.executing = False
    
    def execute(self):
        self.executing = True
        while self.executing:
            if not self.playing:
                # if self.death_count == 0:
                    self.show_menu()
                # else:
                #     self.show_replay()
        pygame.quit()
    
    def run(self):
        # Game loop: events - update - draw
        self.playing = True
        self.obstacle_manager.reset_obstacules()
        while self.playing:
            self.events()
            self.update()
            self.draw()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.executing = False
                

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        # if self.death_count >= 1:
        #     self.player.lifes -= 1
        self.cloud.update(self)
        self.obstacle_manager.update(self.game_speed, self.player, self.on_death)
        self.power_up_manager.update(self.game_speed, self.score.points, self.player)
        self.score.update(self)

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((128, 128, 128))
        self.draw_background()
        self.cloud.draw(self.screen)
        self.player.draw(self.screen)
        self.player.draw_life(self.screen)
        self.player.draw_active_power_uo(self.screen)
        
        self.obstacle_manager.draw(self.screen)
        self.power_up_manager.draw(self.screen)
        self.score.draw(self.screen)
        
        pygame.display.update()
        pygame.display.flip()
        

    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed

    def print_game (self, text_cadena, x_pos_message, y_pos_message):
         font = pygame.font.Font(FONT_STYLE, 30)
         message = font.render(text_cadena, True, (0, 0, 0))
         message_rect = message.get_rect()
         message_rect.center = (x_pos_message, y_pos_message)
         self.screen.blit(message, message_rect)    

    def show_menu(self):
        self.screen.fill((255, 255, 255))
        half_screen_width = SCREEN_WIDTH // 2
        half_screen_height = SCREEN_HEIGHT // 2
        
        if self.player.lifes > 0:
          
            self.screen.blit(DINO_START, (half_screen_width - 40, half_screen_height - 120))
            self.print_game("Press any key to start", half_screen_width, half_screen_height + 40)
            self.print_game(f"your lifes: {self.player.lifes}", half_screen_width, half_screen_height + 120)
        elif self.death_count >= 1:
         
            #self.print_game("Press any key to continue", half_screen_width, half_screen_height)
            self.screen.blit(GAME_OVER,(half_screen_width - 180, half_screen_height - 120));
            self.print_game("Press any key to continue", half_screen_width, half_screen_height + 40)
            self.print_game(f"your score is: {self.score.points}", half_screen_width, half_screen_height + 40)
            
            
            self.screen.blit(BOTON_RESET,(half_screen_width - 40, half_screen_height - 60));
            
        pygame.display.update()
        
        self.handle_menu_events()
    
    def show_replay(self):
        pass
    
    
    def handle_menu_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.executing = False
            elif event.type == pygame.KEYDOWN:
                self.score.points = 0
                self.game_speed = 20
                self.power_up_manager.reset_power_ups()
                self.player.lifes = 5
                self.run()
            
    
    def on_death(self):
        has_shield = self.player.type == SHIELD_TYPE or self.player.type == HAMMER_TYPE
        if not has_shield:
            self.player.on_dino_dead()
            self.draw()
            self.death_count += 1
            self.player.lifes -= 1
            self.playing = False
            
        return not has_shield 