import sys
import pygame
import constants
from Output import Output
from bigseed import BigSeed
from ghost import Ghost, Gannibal, Stalker, Debil
from seed import Seed
import pygame.gfxdraw
import highscore
import time
from datetime import timedelta
from berry import Berry
import Results


class Pacman:
    def __init__(self):
        self.img_path = "images/pacman/right_1.png"
        self.img = pygame.image.load(self.img_path)
        self.img = pygame.transform.scale(self.img, (16, 16))
        self.img_rect = self.img.get_rect()
        self.img_rect.x = 406
        self.img_rect.y = 454
        self.img_angle = 0
        self.right = False
        self.left = False
        self.up = False
        self.down = False
        self.next_x = self.img_rect.x
        self.next_y = self.img_rect.y
        self.surf = pygame.transform.rotate(self.img, self.img_angle)
        self.next_direct = 0  # 1=Right -1=Left 2=Up -2=Down

    def rotate(self, angle):
        self.img_angle = angle % 360
        self.surf = pygame.transform.rotate(self.img, self.img_angle)

    def to_sprite(self):
        s = pygame.sprite.Sprite()
        s.image = self.img
        s.rect = self.img_rect
        return s


class MAP:

    def __init__(self):
        pygame.init()
        pygame.font.init()
        self.pacman = Pacman()
        self.map_start = time.monotonic()
        self.Highscore = highscore.Highscore()
        self.positionD = 380, 306
        self.positionG = 400, 306
        self.positionS = 360, 306
        self.position = 380, 290
        self.Ghost = Ghost(self.position)
        self.Gannibal = Gannibal(self.positionG)
        self.Stalker = Stalker(self.positionS)
        self.Debil = Debil(self.positionD)
        self.Output = Output()
        self.Seed = Seed()
        self.Berry = Berry()
        self.bigseed = BigSeed()
        self.gameover = False
        self.map = [[2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
                    [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
                    [2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2],
                    [2, 2, 2, 2, 2, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2],
                    [2, 2, 2, 2, 2, 2, 1, 3, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 3, 1, 2],
                    [2, 2, 2, 2, 2, 2, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 2],
                    [2, 2, 2, 2, 2, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2],
                    [2, 2, 2, 2, 2, 2, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 2],
                    [2, 2, 2, 2, 2, 2, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 2],
                    [2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 0, 1, 1, 1, 2, 1, 2, 1, 1, 1, 0, 1, 1, 1, 1, 2],
                    [2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 0, 1, 2, 2, 2, 2, 2, 2, 2, 1, 0, 1, 2, 2, 2, 2],
                    [2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 0, 1, 2, 1, 1, 1, 1, 1, 2, 1, 0, 1, 1, 1, 1, 2],
                    [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 2, 2, 1, 2, 2, 2, 1, 2, 2, 0, 2, 2, 2, 2, 2],
                    [2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 0, 1, 2, 1, 1, 1, 1, 1, 2, 1, 0, 1, 1, 1, 1, 2],
                    [2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 0, 1, 2, 2, 2, 2, 2, 2, 2, 1, 0, 1, 2, 2, 2, 2],
                    [2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 0, 1, 2, 1, 1, 1, 1, 1, 2, 1, 0, 1, 1, 1, 1, 2],
                    [2, 2, 2, 2, 2, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2],
                    [2, 2, 2, 2, 2, 2, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 2],
                    [2, 2, 2, 2, 2, 2, 1, 3, 0, 1, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 1, 0, 3, 1, 2],
                    [2, 2, 2, 2, 2, 2, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 2],
                    [2, 2, 2, 2, 2, 2, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 2],
                    [2, 2, 2, 2, 2, 2, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 2],
                    [2, 2, 2, 2, 2, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2],
                    [2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2]]

    def move(self, screen):
        for event in pygame.event.get():  # Получение всех событий
            if event.type == pygame.QUIT:  # Событие выхода
                self.gameover = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    if self.pacman.img_rect.y / 25 == 12.16 and self.pacman.img_rect.x / 25 >= 23.24:
                        self.pacman.img_rect.y = 304
                        self.pacman.img_rect.x = 156
                        screen.blit(self.pacman.img, self.pacman.img_rect)
                    if self.map[int(self.pacman.img_rect.y / 25)][int(self.pacman.img_rect.x / 25) + 1] != 1:

                        self.pacman.right = True
                        self.pacman.left = False
                        self.pacman.up = False
                        self.pacman.down = False
                        self.pacman.next_direct = 0
                    else:
                        self.pacman.next_direct = 1
                if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    if self.pacman.img_rect.y / 25 == 12.16 and self.pacman.img_rect.x / 25 <= 7.24:
                        self.pacman.img_rect.y = 304
                        self.pacman.img_rect.x = 606
                        screen.blit(self.pacman.img, self.pacman.img_rect)
                    if self.map[int(self.pacman.img_rect.y / 25)][int(self.pacman.img_rect.x / 25) - 1] != 1:
                        self.pacman.left = True
                        self.pacman.right = False
                        self.pacman.up = False
                        self.pacman.down = False
                        self.pacman.next_direct = 0
                    else:
                        self.pacman.next_direct = -1
                if event.key == pygame.K_w or event.key == pygame.K_UP:
                    if self.map[int(self.pacman.img_rect.y / 25) - 1][int(self.pacman.img_rect.x / 25)] != 1:
                        self.pacman.up = True
                        self.pacman.right = False
                        self.pacman.left = False
                        self.pacman.down = False
                        self.pacman.next_direct = 0
                    else:
                        self.pacman.next_direct = 2
                if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    if self.map[int(self.pacman.img_rect.y / 25) + 1][int(self.pacman.img_rect.x / 25)] != 1:
                        self.pacman.down = True
                        self.pacman.right = False
                        self.pacman.left = False
                        self.pacman.up = False
                        self.pacman.next_direct = 0
                    else:
                        self.pacman.next_direct = -2
        if self.pacman.next_direct != 0:
            if self.map[int(self.pacman.img_rect.y / 25) + 1][int(self.pacman.img_rect.x / 25)] != 1 and self.pacman.next_direct == -2:
                self.pacman.down = True
                self.pacman.right = False
                self.pacman.left = False
                self.pacman.up = False
                self.pacman.next_direct = 0
            if self.map[int(self.pacman.img_rect.y / 25) - 1][int(self.pacman.img_rect.x / 25)] != 1 and self.pacman.next_direct == 2:
                self.pacman.up = True
                self.pacman.right = False
                self.pacman.left = False
                self.pacman.down = False
                self.pacman.next_direct = 0
            if self.map[int(self.pacman.img_rect.y / 25)][int(self.pacman.img_rect.x / 25) - 1] != 1 and self.pacman.next_direct == -1:
                self.pacman.left = True
                self.pacman.right = False
                self.pacman.up = False
                self.pacman.down = False
                self.pacman.next_direct = 0
            if self.map[int(self.pacman.img_rect.y / 25)][int(self.pacman.img_rect.x / 25) + 1] != 1 and self.pacman.next_direct == 1:
                self.pacman.right = True
                self.pacman.left = False
                self.pacman.up = False
                self.pacman.down = False
                self.pacman.next_direct = 0
        if self.map[int(self.pacman.img_rect.y / 25)][int(self.pacman.img_rect.x / 25)] == 0:
            self.map[int(self.pacman.img_rect.y / 25)][int(self.pacman.img_rect.x / 25)] = 2
            self.Output.seed_score()
        if self.map[int(self.pacman.img_rect.y / 25)][int(self.pacman.img_rect.x / 25)] == 3:
            self.map[int(self.pacman.img_rect.y / 25)][int(self.pacman.img_rect.x / 25)] = 2
            self.Output.bigseed_score()
        if self.map[int(self.pacman.img_rect.y / 25)][int(self.pacman.img_rect.x / 25)] == 8:
            self.map[int(self.pacman.img_rect.y / 25)][int(self.pacman.img_rect.x / 25)] = 5
            self.Output.berry_score()
        s1 = self.pacman.to_sprite()
        s2 = self.Ghost.to_sprite()
        s3 = self.Stalker.to_sprite()
        s4 = self.Debil.to_sprite()
        s5 = self.Gannibal.to_sprite()
        if pygame.sprite.collide_mask(s1, s2) or pygame.sprite.collide_mask(s1, s3) or pygame.sprite.collide_mask(s1, s4) or pygame.sprite.collide_mask(s1, s5):  # коллизия с ghost
            self.Output.death()
            self.pacman.img_rect.x = 406
            self.pacman.img_rect.y = 454
            self.pacman.rotate(0)
            self.draw(screen, 0, 0)#
        self.Berry.draw(screen, self.map)
        if self.pacman.down and self.map[int(self.pacman.img_rect.y / 25) + 1][int(self.pacman.img_rect.x / 25)] != 1:
            self.pacman.rotate(270)
            self.draw(screen, 0, 25)
        elif self.pacman.up and self.map[int(self.pacman.img_rect.y / 25) - 1][int(self.pacman.img_rect.x / 25)] != 1:
            self.pacman.rotate(90)
            self.draw(screen, 0, -25)
        elif self.pacman.right and self.map[int(self.pacman.img_rect.y / 25)][int(self.pacman.img_rect.x / 25) + 1] != 1:
            self.pacman.rotate(0)
            self.draw(screen, 25, 0)
        elif self.pacman.left and self.map[int(self.pacman.img_rect.y / 25)][int(self.pacman.img_rect.x / 25) - 1] != 1:
            self.pacman.rotate(180)
            self.draw(screen, -25, 0)
        self.Ghost.draw(screen)
        self.Debil.draw(screen)
        self.Stalker.draw(screen)
        self.Gannibal.draw(screen)

    def update_seeds(self):
        for i in range(len(self.map)):
            tmp = self.map[i]
            for j in range(len(tmp)):
                if self.map[i][j] == 5:
                    self.map[i][j] = 0
                elif self.map[i][j] == 6:
                    self.map[i][j] = 3

    def draw_map(self, screen):
        for y in range(len(self.map)):
            for x in range(len(self.map[y])):
                if timedelta(seconds=time.monotonic() - self.map_start).seconds <= 10:
                    self.map[11][15] = 2
                if x == 15 and y == 11 and timedelta(seconds=time.monotonic() - self.map_start).seconds <= 10:
                    pygame.draw.line(screen, (255, 255, 255), (25 * x, y * 25 + 12), (25 * x + 25, y * 25 + 12), 5)
                elif self.map[y][x] == 1:
                    pygame.draw.rect(screen, constants.FIELD_COLOR, (x * 25, y * 25, 25, 25))
                elif self.map[y][x] == 0:
                    tmp = Seed()
                    tmp.draw(screen, (x * 25 + 12, y * 25 + 12))
                elif self.map[y][x] == 3:
                    tmp1 = BigSeed()
                    tmp1.draw(screen, (x * 25 + 12, y * 25 + 12))
        graph = pygame.draw.rect
        graph(screen, constants.BLACK, [155, 55, 465, 15], 0)
        graph(screen, constants.BLACK, [155, 55, 15, 190], 0)
        graph(screen, constants.BLACK, [605, 55, 15, 190], 0)
        graph(screen, constants.BLACK, [380, 55, 15, 90], 0)
        graph(screen, constants.BLACK, [380, 180, 15, 65], 0)
        graph(screen, constants.BLACK, [330, 180, 115, 15], 0)
        graph(screen, constants.BLACK, [155, 580, 465, 15], 0)
        graph(screen, constants.BLACK, [155, 380, 15, 200], 0)
        graph(screen, constants.BLACK, [605, 380, 15, 200], 0)
        graph(screen, constants.BLACK, [380, 380, 15, 65], 0)
        graph(screen, constants.BLACK, [330, 380, 115, 15], 0)
        graph(screen, constants.BLACK, [380, 480, 15, 65], 0)
        graph(screen, constants.BLACK, [330, 480, 115, 15], 0)
        graph(screen, constants.BLACK, [330, 330, 115, 15], 0)
        graph(screen, constants.BLACK, [530, 330, 90, 15], 0)
        graph(screen, constants.BLACK, [155, 330, 90, 15], 0)
        graph(screen, constants.BLACK, [530, 380, 90, 15], 0)
        graph(screen, constants.BLACK, [155, 380, 90, 15], 0)
        graph(screen, constants.BLACK, [530, 280, 90, 15], 0)
        graph(screen, constants.BLACK, [155, 280, 90, 15], 0)
        graph(screen, constants.BLACK, [530, 230, 90, 15], 0)
        graph(screen, constants.BLACK, [155, 230, 90, 15], 0)
        graph(screen, constants.BLACK, [230, 245, 15, 35], 0)
        graph(screen, constants.BLACK, [230, 345, 15, 35], 0)
        graph(screen, constants.BLACK, [530, 230, 15, 65], 0)
        graph(screen, constants.BLACK, [530, 330, 15, 65], 0)
        graph(screen, constants.BLACK, [205, 530, 140, 15], 0)
        graph(screen, constants.BLACK, [430, 530, 140, 15], 0)
        graph(screen, constants.BLACK, [280, 480, 15, 65], 0)
        graph(screen, constants.BLACK, [480, 480, 15, 65], 0)
        graph(screen, constants.BLACK, [280, 430, 65, 15], 0)
        graph(screen, constants.BLACK, [430, 430, 65, 15], 0)
        graph(screen, constants.BLACK, [230, 430, 15, 65], 0)
        graph(screen, constants.BLACK, [530, 430, 15, 65], 0)
        graph(screen, constants.BLACK, [230, 430, -25, 15], 0)
        graph(screen, constants.BLACK, [530, 430, 40, 15], 0)
        graph(screen, constants.BLACK, [170, 480, 25, 15], 0)
        graph(screen, constants.BLACK, [580, 480, 35, 15], 0)
        graph(screen, constants.BLACK, [205, 105, 40, 40], 0)
        graph(screen, constants.BLACK, [205, 180, 40, 15], 0)
        graph(screen, constants.BLACK, [530, 180, 40, 15], 0)
        graph(screen, constants.BLACK, [530, 105, 40, 40], 0)
        graph(screen, constants.BLACK, [280, 105, 65, 40], 0)
        graph(screen, constants.BLACK, [430, 105, 65, 40], 0)
        graph(screen, constants.BLACK, [280, 180, 15, 115], 0)
        graph(screen, constants.BLACK, [480, 180, 15, 115], 0)
        graph(screen, constants.BLACK, [280, 230, 65, 15], 0)
        graph(screen, constants.BLACK, [480, 230, -50, 15], 0)
        graph(screen, constants.BLACK, [280, 330, 15, 65], 0)
        graph(screen, constants.BLACK, [480, 330, 15, 65], 0)
        graph(screen, constants.BLACK, [330, 280, 15, 55], 0)
        graph(screen, constants.BLACK, [430, 280, 15, 55], 0)
        graph(screen, constants.BLACK, [330, 280, 40, 15], 0)
        graph(screen, constants.BLACK, [430, 280, -25, 15], 0)

    def start(self, screen):
        font = pygame.font.SysFont('Helvetica', 27, True)
        over = False
        cnt = 0
        while not over:
            screen.fill(constants.BLACK)
            screen.blit(self.pacman.img, self.pacman.img_rect)
            self.draw_map(screen)
            self.Ghost.draw(screen)
            self.Stalker.draw(screen)
            self.Gannibal.draw(screen)
            self.Debil.draw(screen)
            self.Output.show(screen)
            for event in pygame.event.get():  # Получение всех событий
                if event.type == pygame.QUIT:  # Событие выхода
                    over = True
                elif event.type == pygame.KEYDOWN:
                    over = True
            if cnt == 998:
                over = True
            screen.blit(font.render('READY! {}'.format(3 - int(cnt // 333)), False, (244, 194, 13)), (340, 345))
            pygame.display.flip()
            cnt += 1
        screen.fill(constants.BLACK)
        screen.blit(self.pacman.img, self.pacman.img_rect)
        self.draw_map(screen)
        self.Ghost.draw(screen)
        self.Stalker.draw(screen)
        self.Gannibal.draw(screen)
        self.Debil.draw(screen)
        self.Output.show(screen)
        pygame.display.flip()

    def draw(self, screen, x, y):
        if x == 0:
            if y < 0:
                for i in range(-y):
                    self.pacman.img_rect.y -= 1
                    screen.fill(constants.BLACK)
                    self.draw_map(screen)
                    self.Ghost.draw(screen)
                    self.Stalker.draw(screen)
                    self.Gannibal.draw(screen)
                    self.Debil.draw(screen)
                    self.Output.show(screen)
                    self.Berry.draw(screen, self.map)
                    screen.blit(self.pacman.surf, self.pacman.img_rect)
                    pygame.display.flip()
                    pygame.time.wait(5)
            elif y > 0:
                for i in range(y):
                    self.pacman.img_rect.y += 1
                    screen.fill(constants.BLACK)
                    self.draw_map(screen)
                    self.Ghost.draw(screen)
                    self.Stalker.draw(screen)
                    self.Gannibal.draw(screen)
                    self.Debil.draw(screen)
                    self.Output.show(screen)
                    self.Berry.draw(screen, self.map)
                    screen.blit(self.pacman.surf, self.pacman.img_rect)
                    pygame.display.flip()
                    pygame.time.wait(5)
            else:
                screen.fill(constants.BLACK)
                self.draw_map(screen)
                self.Ghost.draw(screen)
                self.Stalker.draw(screen)
                self.Gannibal.draw(screen)
                self.Debil.draw(screen)
                self.Output.show(screen)
                self.Berry.draw(screen, self.map)
                screen.blit(self.pacman.surf, self.pacman.img_rect)
                pygame.display.flip()
                pygame.time.wait(5)
        elif x < 0:
            for i in range(-x):
                self.pacman.img_rect.x -= 1
                screen.fill(constants.BLACK)
                self.draw_map(screen)
                self.Ghost.draw(screen)
                self.Stalker.draw(screen)
                self.Gannibal.draw(screen)
                self.Debil.draw(screen)
                self.Output.show(screen)
                self.Berry.draw(screen, self.map)
                if self.pacman.img_rect.y / 25 == 12.16 and self.pacman.img_rect.x / 25 == 7.24:
                    self.pacman.img_rect.y = 304
                    self.pacman.img_rect.x = 606
                    screen.blit(self.pacman.img, self.pacman.img_rect)
                    self.Output.show(screen)
                else:
                    screen.blit(self.pacman.surf, self.pacman.img_rect)
                    self.Output.show(screen)
                pygame.display.flip()
                pygame.time.wait(5)
        else:
            for i in range(x):
                self.pacman.img_rect.x += 1
                screen.fill(constants.BLACK)
                self.draw_map(screen)
                self.Ghost.draw(screen)
                self.Stalker.draw(screen)
                self.Gannibal.draw(screen)
                self.Debil.draw(screen)
                self.Output.show(screen)
                self.Berry.draw(screen, self.map)
                if self.pacman.img_rect.y / 25 == 12.16 and self.pacman.img_rect.x / 25 == 23.24:
                    self.pacman.img_rect.y = 304
                    self.pacman.img_rect.x = 156
                    screen.blit(self.pacman.img, self.pacman.img_rect)
                    self.Output.show(screen)
                else:
                    screen.blit(self.pacman.surf, self.pacman.img_rect)
                    self.Output.show(screen)
                pygame.display.flip()
                pygame.time.wait(5)
        black = pygame.Surface((18, 18))
        black.fill((0, 0, 0))
        if self.map[int(self.pacman.img_rect.y / 25)][int(self.pacman.img_rect.x / 25)] == 0:
            self.map[int(self.pacman.img_rect.y / 25)][int(self.pacman.img_rect.x / 25)] = 5
            screen.blit(black, (self.pacman.img_rect.x, self.pacman.img_rect.y))
            screen.blit(self.pacman.surf, self.pacman.img_rect)
            self.Output.seed_score()
            pygame.display.flip()
        if int(self.pacman.img_rect.y / 25) == self.Berry.y and int(self.pacman.img_rect.x / 25) == self.Berry.x:
            self.Output.berry_score()
            self.map[self.Berry.y][self.Berry.x] = 5
            self.Berry.exist = 0
            self.Berry.end = 0
            self.Berry.draw(screen, self.map)
            screen.blit(black, (self.pacman.img_rect.x - 1, self.pacman.img_rect.y - 1))
            screen.blit(self.pacman.surf, self.pacman.img_rect)
            pygame.display.flip()
        if self.map[int(self.pacman.img_rect.y / 25)][int(self.pacman.img_rect.x / 25)] == 3 and (self.Gannibal.fear or self.Stalker.fear or self.Ghost.fear or self.Debil.fear):
            self.Ghost.time_left += 10
            self.Debil.time_left += 10
            self.Stalker.time_left += 10
            self.Gannibal.time_left += 10
            self.Gannibal.draw(screen)
            self.Stalker.draw(screen)
            self.Debil.draw(screen)
            self.Ghost.draw(screen)
            screen.blit(black, (self.pacman.img_rect.x - 1, self.pacman.img_rect.y - 1))
            screen.blit(self.pacman.surf, self.pacman.img_rect)
            pygame.display.flip()
        if self.map[int(self.pacman.img_rect.y / 25)][int(self.pacman.img_rect.x / 25)] == 3:
            self.map[int(self.pacman.img_rect.y / 25)][int(self.pacman.img_rect.x / 25)] = 6
            self.Output.bigseed_score()
            self.Gannibal.fear = True
            self.Stalker.fear = True
            self.Debil.fear = True
            self.Ghost.fear = True
            screen.blit(black, (self.pacman.img_rect.x - 1, self.pacman.img_rect.y - 1))
            screen.blit(self.pacman.surf, self.pacman.img_rect)
            pygame.display.flip()

    def run(self, screen):
        self.start(screen)
        while not self.gameover:
            self.move(screen)
            pygame.display.flip()
            if self.Output.score % 1720 == 0:
                self.update_seeds()
            if self.Output.dead == 1:
                self.gameover = True
                with open('nickname.txt', 'r') as f:
                    self.Highscore.insert(f.readline(), self.Output.scorenum)
                    with open('nickname.txt', 'w') as f1:
                        f1.write('\n')
                res = Results.Results()
                res.draw(screen)
                game = True
                while game:
                    for events in pygame.event.get():
                        if events.type == pygame.KEYDOWN:
                            if events.key == pygame.K_ESCAPE or events.key == pygame.K_SPACE:
                                game = False
                        elif events.type == pygame.QUIT:
                            game = False
        sys.exit()
