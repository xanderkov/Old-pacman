import pygame
import constants


class Results:
    def __init__(self):
        self.data = []
        self.font = pygame.font.SysFont('Comic Sans', 50, True)
        with open('highscores.txt', 'r') as f:
            for line in f:
                self.data.append(line.replace('\n', ''))

    def draw(self, screen):
        screen.fill(constants.BLACK)
        msg = self.font.render('HIGHSCORE:', False, constants.WHITE)
        screen.blit(msg, (constants.WIDTH / 3, 10))
        for i in range(len(self.data)):
            if i == 0:
                color = constants.GOOGLE_GREEN
            elif i == 1:
                color = constants.GOOGLE_YELLOW
            elif i == 2:
                color = constants.GOOGLE_BLUE
            else:
                color = constants.WHITE
            msg = self.font.render(' ' + str(i+1) + '.' + self.data[i], False, color)
            screen.blit(msg, (constants.WIDTH/4, i*55 + 65))
        pygame.display.flip()
