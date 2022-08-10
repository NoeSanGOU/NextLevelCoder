import pygame
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.utils.constants import SMALL_CACTUS
#TAREA:
from dino_runner.utils.constants import LARGE_CACTUS
class ObstacleManager:
    def __init__(self):
        self.obstacles = []

    def update(self,game):
    #si la longitud es cero , deberia añadir un obstaculo
        #rount = 0
        if len(self.obstacles) == 0:
            self.obstacles.append(Cactus(SMALL_CACTUS)) or self.obstacles.append(Cactus(LARGE_CACTUS))

        
            #zip() chain()
            rount +=1
            #aniadir otros obstaculos(cactus largos )
            #self.obstacles.append(Cactus(SMALL_CACTUS))


        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect):
                pygame.time.delay(500)
                game.playing = False
                break

    #Aqui deberia dbujar el obstaculo:
    def draw(self,screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)