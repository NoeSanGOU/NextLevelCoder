import pygame
import random

from dino_runner.components.obstacles.cactus import Cactus

class ObstacleManager:
    def __init__(self):
        self.obstacles = []

    
    def update(self,game):
        if len(self.obstacles) == 0:
            cactus_type = "SMALL" if random.randint(0,1) == 0 else "LARGE"
            self.obstacles.append(Cactus(cactus_type)) 

        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect):
                if not game.player.shield:
                    pygame.time.delay(500)
                    game.playing = False
                    game.death_count += 1
                else:
                    self.obstacles.remove(obstacle)
                break

    #Aqui deberia dbujar el obstaculo:
    def draw(self,screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)

    def reset_osbstacles(self):
        self.obstacles = []
