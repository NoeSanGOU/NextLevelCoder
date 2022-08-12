import pygame
from dino_runner.components.obstacles.obstacle_manager import ObstacleManager
from dino_runner.components.dinosaur import Dinosaur
from dino_runner.components.power_ups.power_up_manager import PowerUpManager
from dino_runner.utils.constants import BG, ICON, RUNNING, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS
from dino_runner.utils.text_utils import draw_message_component



class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.player = Dinosaur()
        self.obstacle_manager = ObstacleManager()
        self.power_up_manager = PowerUpManager()
        self.playing = False
        self.running = False
        self.game_speed = 20
        self.x_pos_bg = 0
        self.y_pos_bg = 380

        self.points = 0
        self.death_count = 0

    def execute(self):
        self.running = True
        while self.running :
            if not self.playing:
                self.show_menu() 

        pygame.display.quit()
        pygame.quit()

    def run(self):
        # Game loop: events - update - draw
        self.obstacle_manager.reset_osbstacles()
        self.power_up_manager.reset_power_ups()
        self.playing = True
        self.game_speed = 20
        self.points = 0
        while self.playing:
            self.events()
            self.update()
            self.draw()
        

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running= False

    def update(self):
        self.update_score()
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        self.obstacle_manager.update(self)
        self.power_up_manager.update(self.points, self.game_speed, self.player)
        

    def update_score(self):
        self.points += 1
        if self.points & 100 == 0:
            self.game_speed +=1

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_score()
        self.draw_background()
        self.player.draw(self.screen)
        self.player.check_invincibility(self.screen)
        self.obstacle_manager.draw(self.screen)
        self.power_up_manager.draw(self.screen)
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
   
    def draw_score(self):
        draw_message_component(
            f"Points: {self.points}",
            self.screen,
            font_size=22,
            pos_x_center=1000,
            pos_y_center=50   
        )
        
    def handle_key_events_on_menu(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing == False
                self.running == False
            elif event.type == pygame.KEYDOWN:
                self.run()
    
    def show_menu(self):
        self.screen.fill((255,153,153))#change color 
        half_screen_height = SCREEN_HEIGHT // 2
        half_screen_width = SCREEN_WIDTH // 2
        
        if self.death_count == 0:
            draw_message_component("Press any key to start", self.screen)#True, (128,0,128)  
        elif self.death_count > 0:
            draw_message_component("Press any key to restart", self.screen)
            draw_message_component(
                f"Your Score is: {self.points}",
                self.screen,
                pos_y_center=half_screen_height + 50
            )
            draw_message_component(
                f"Death Count is: {self.death_count}",
                self.screen,
                pos_y_center=half_screen_height + 100
            )
           
        self.screen.blit(RUNNING[0], (half_screen_width - 20, half_screen_height - 140))

        pygame.display.update()
        self.handle_key_events_on_menu()
