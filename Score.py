import pygame


class Score:
    def __init__(self):
        self.scorenum = 0

    def show(self, screen):
        font = pygame.font.SysFont('Helvetica', 30, True)
        s = self.scorenum
        ScoreRender = font.render('SCORE:{}'.format(s), False, (255, 255, 255))
        screen.blit(ScoreRender, (500, 13))

    def seed_score(self):
        self.scorenum += 10

    def bigseed_score(self):
        self.scorenum += 50

    def berry_score(self):
        self.scorenum += 100

    def ghost(self, n):
        self.scorenum += 100*2**n