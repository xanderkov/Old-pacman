import constants
import pygame
class BigSeed:

    def __init__(self):
        self.score = 50

    def draw(self, screen, position):
        pygame.draw.circle(screen, constants. WHITE, position, 7)

