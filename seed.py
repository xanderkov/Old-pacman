import pygame
import constants


class Seed:

    def __init__(self):
        self.score = 10
        self.score = 200


    def draw(self, screen, position):
        pygame.draw.circle(screen, constants.SEED_YELLOW, position, 2)

    def eating_sound(self):
        pygame.mixer.music.load("sounds/seed_eating.mp3")
        pygame.mixer.music.play(0)
        pygame.mixer.pre_init(44100, -16, 2, 2048)
        pygame.mixer.quit()
        pygame.mixer.init()
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
