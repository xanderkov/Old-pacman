import pygame


class Lives:
    def __init__(self):
        self.count = 3
        self.img = pygame.image.load('images/live.png')
        self.img = pygame.transform.scale(self.img, (30, 30))

    def draw(self, screen):
        for i in range(self.count - 1):
            screen.blit(self.img, (3 + i * 32, 560))

    def death(self):
        self.count == self.count - 1
