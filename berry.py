import pygame
from datetime import timedelta
import time
import random


class Berry:
    def __init__(self):
        self.img_path = "images/berry.png"
        self.img = pygame.image.load(self.img_path)
        self.img = pygame.transform.scale(self.img, (16, 16))
        self.score = 100
        self.start = 0
        self.x = 0
        self.y = 0
        self.end = 0
        self.exist = 0

    def draw(self, screen, Map):
        coords = []
        for i in range(len(Map)):
            for j in range(len(Map[i])):
                if Map[i][j] == 5:
                    coords.append([j, i])
        if len(coords) != 0:
            if not self.exist:
                if not self.end:
                    self.y, self.x = -1, -1
                    self.end = time.monotonic()
                if timedelta(seconds=time.monotonic() - self.end).seconds >= 20:
                    r = random.randint(0, len(coords) - 1)
                    self.x = coords[r][0]
                    self.y = coords[r][1]
                    screen.blit(self.img, (self.x * 25 + 2, self.y * 25 + 2))
                    self.start = time.monotonic()
                    self.exist = 1
            else:
                if timedelta(seconds=time.monotonic() - self.start).seconds >= 10:
                    black = pygame.Surface((16, 16))
                    self.end = time.monotonic()
                    black.fill((0, 0, 0))
                    screen.blit(black, (self.x * 25 + 2, self.y * 25 + 2))
                    self.exist = 0
                else:
                    if timedelta(seconds=time.monotonic() - self.end).seconds >= 20:
                        screen.blit(self.img, (self.x * 25 + 2, self.y * 25 + 2))
                        self.exist = 1