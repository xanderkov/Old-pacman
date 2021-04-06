import pygame


class Output:
    def __init__(self):
        self.scorenum = 0
        self.score = 0
        self.count = 3
        self.img = pygame.image.load('images/live.png')
        self.img = pygame.transform.scale(self.img, (70, 70))
        self.dead = 0 # 1 / 0

    def show(self, screen):
        if self.count > 0:
            font = pygame.font.SysFont('Helvetica', 30, True)
            s = self.scorenum
            ScoreRender = font.render('SCORE:{}'.format(s), False, (255, 255, 255))
            for i in range(self.count):
                screen.blit(self.img, (3 + i * 32, 50))
            screen.blit(ScoreRender, (13, 13))
        else:
            font = pygame.font.SysFont('Helvetica', 20, True)
            screen.blit(font.render('GAME    OVER!', False, (255, 0, 0)), (330, 353))
            pygame.display.flip()
            over = False
            cnt = 0
            while not over:
                for event in pygame.event.get():  # Получение всех событий
                    if event.type == pygame.QUIT:  # Событие выхода
                        over = True
                if cnt == 4000:
                    over = True
                pygame.time.wait(1)
                cnt += 1
            #time.sleep(5)
            self.dead = 1

    def seed_score(self):
        self.scorenum += 10
        self.score += 10

    def bigseed_score(self):
        self.scorenum += 50
        self.score += 50

    def berry_score(self):
        self.scorenum += 100

    def ghost(self, n):
        self.scorenum += 100*2**n
        self.score += 100*2**n

    def death(self):
        self.count = self.count - 1
