import pygame
import random
import time
from datetime import timedelta


class Ghost:
    def __init__(self, position):
        self.path = "red/"
        self.image = pygame.image.load("images/ghosts/red/right_1.png")
        self.image = pygame.transform.scale(self.image, (16, 16))
        self.geometry = self.image.get_rect()
        self.geometry.x, self.geometry.y = position[0], position[1]
        self.speed = 0
        self.id = "R"
        self.panic_start = 0
        self.direction = 'RIGHT'
        self.fear = False
        self.direction_options = ['UP', 'DOWN', 'RIGHT', 'LEFT']
        self.time_left = 10

    def draw(self, screen):
        if self.fear and not self.panic_start:
            self.panic_start = time.monotonic()
        elif self.fear and timedelta(seconds=time.monotonic() - self.panic_start).seconds < self.time_left:
            self.fear = True
            self.image = pygame.image.load("images/ghosts/frightened/g_1.png")
            self.image = pygame.transform.scale(self.image, (16, 16))
        else:
            self.panic_start = 0
            self.time_left = 10
            self.fear = False
            if self.direction == 'LEFT':
                self.image = pygame.image.load("images/ghosts/" + self.path + "left_1.png")
            elif self.direction == 'RIGHT':
                self.image = pygame.image.load("images/ghosts/" + self.path + "right_1.png")
            elif self.direction == 'UP':
                self.image = pygame.image.load("images/ghosts/" + self.path + "up_1.png")
            elif self.direction == 'DOWN':
                self.image = pygame.image.load("images/ghosts/" + self.path + "down_1.png")
            else:
                self.image = pygame.image.load("images/ghosts/" + self.path + "right_1.png")
        screen.blit(self.image, self.geometry)

    def check_ghost_collision(self):
        pass

    def shift(self):
        if self.direction == 'LEFT':
            self.geometry.x -= self.speed
        elif self.direction == 'UP':
            self.geometry.y -= self.speed
        elif self.direction == 'RIGHT':
            self.geometry.x += self.speed
        elif self.direction == 'DOWN':
            self.geometry.y += self.speed

    def trajectory(self):
        pass #Рассчитывает траекторию. Пока не разберусь с расчетом кратчайшего пути в графе, сделаю просто рандом на каждом повороте.

    def to_sprite(self):
        s = pygame.sprite.Sprite()
        s.image = self.image
        s.rect = self.geometry
        return s


class Gannibal(Ghost):
    def __init__(self, position):
        self.id = "O"
        self.path = "orange/"
        self.image = pygame.image.load("images/ghosts/orange/right_1.png")
        self.image = pygame.transform.scale(self.image, (16, 16))
        self.geometry = self.image.get_rect()
        self.geometry.x, self.geometry.y = position[0], position[1]
        self.speed = 0
        self.direction = 'RIGHT'
        self.fear = False
        self.time_left = 10
        self.direction_options = ['UP', 'DOWN', 'RIGHT', 'LEFT']

    def trajectory(self):
        pass #Будет искать самый короткий путь до пакмана в графе -_-

    def to_sprite(self):
        s = pygame.sprite.Sprite()
        s.image = self.image
        s.rect = self.geometry
        return s


class Stalker(Ghost):
    def __init__(self, position):
        self.path = "blue/"
        self.id = "B"
        self.image = pygame.image.load("images/ghosts/blue/right_1.png")
        self.image = pygame.transform.scale(self.image, (16, 16))
        self.geometry = self.image.get_rect()
        self.geometry.x, self.geometry.y = position[0], position[1]
        self.speed = 0
        self.direction = 'RIGHT'
        self.fear = False
        self.time_left = 10
        self.direction_options = ['UP', 'DOWN', 'RIGHT', 'LEFT']

    def trajectory(self):
        pass #Будет просто следовать за пакманом каждый шаг

    def to_sprite(self):
        s = pygame.sprite.Sprite()
        s.image = self.image
        s.rect = self.geometry
        return s



class Debil(Ghost):
    def __init__(self, position):
        self.path = "brown/"
        self.id = 'B'
        self.image = pygame.image.load("images/ghosts/brown/right_1.png")
        self.image = pygame.transform.scale(self.image, (16, 16))
        self.geometry = self.image.get_rect()
        self.geometry.x, self.geometry.y = position[0], position[1]
        self.speed = 0
        self.direction = 'RIGHT'
        self.fear = False
        self.time_left = 10
        self.direction_options = ['UP', 'DOWN', 'RIGHT', 'LEFT']

    def trajectory(self):
        pass

    def to_sprite(self):
        s = pygame.sprite.Sprite()
        s.image = self.image
        s.rect = self.geometry
        return s
