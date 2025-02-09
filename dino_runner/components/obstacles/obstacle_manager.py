import random
import pygame
from dino_runner.components.obstacles.bird import Bird
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.utils.constants import (BIRD, CLOUD, LARGE_CACTUS, SMALL_CACTUS)
class ObstacleManager():
    def __init__(self):
        self.obstacles = []
    #agregar el obstaculo bird y mejora del large cactus
    def update(self, game):
        if len(self.obstacles)==0:
            cactus_size = random.randint(0,2)
            if cactus_size==0:
                self.large_cactus=Cactus(LARGE_CACTUS)
                self.large_cactus.rect.y=300
                self.obstacles.append(self.large_cactus)
            elif cactus_size==1:
                self.obstacles.append(Bird(BIRD))
            elif cactus_size==2:
                self.bird = Bird(BIRD)
                self.bird.rect.y=325
                self.obstacles.append(self.bird)
            else:
                self.obstacles.append(Cactus(SMALL_CACTUS))
        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.dino.dino_rect.colliderect(obstacle.rect) and game.dino.shield == False:
                pygame.time.delay(100)
                game.player_heart_manager.reduce_heart()
                if game.player_heart_manager.heart_count >0:
                    self.obstacles.pop()
                    game.dino.has_lives = True
                else:
                    #pygame.time.delay(500)
                    game.dino.has_lives = False
                    game.playing = False
                    game.death_count +=1
                    break
    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)