import random
import pygame
from dino_runner.components.obstacles.cactus import cactus
from dino_runner.utils.constants import (LARGE_CACTUS, SMALL_CACTUS)
class ObstacleManager():
    def __init__(self):
        self.obstacles = []

    def update(self, game):
        if len(self.obstacles)==0:
            cactus_size = random.randint(0,1)
            if cactus_size==0:
                self.obstacles.append(cactus(LARGE_CACTUS))
            else:
                self.obstacles.append(cactus(SMALL_CACTUS))
        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.dino.dino_rect.colliderect(obstacle.rect):
                pygame.time.delay(500)
                game.playing = False
                break
    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)