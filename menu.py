from PyQt5.QtWidgets import QApplication
from pygame.locals import *
import os
import random
from pygame import mixer
import pygame
import pygameMenu
from Results import Results
from pygameMenu.locals import *
import GAME
from input import *
import constants

COLOR_BACKGROUND = (0, 0, 0)
COLOR_YELLOW = (255, 255, 0)
COLOR_WHITE = (255, 255, 255)
FPS = 60.0
WINDOW_SIZE = (800, 600)
mixer.init()
#path_to_music = 'sounds/music/'
#sound = ['1.mp3',
#         '2.mp3',
#         '3.mp3',
#         '4.mp3',
#         '5.mp3',
#         '6.mp3',
#         '7.mp3',
#         '8.mp3']
#pygame.mixer.music.load(path_to_music + sound[random.randint(0, 7)])
#pygame.mixer.music.set_volume(0.1)
#pygame.mixer.music.play()
WINDOW_SIZE = (constants.WIDTH, constants.HEIGHT)

# -----------------------------------------------------------------------------
pygame.init()
logo = pygame.image.load('images/logo.png')
pygame.display.set_icon(logo)
os.environ['SDL_VIDEO_CENTERED'] = '1'
surface = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption('PACMAN')
clock = pygame.time.Clock()
dt = 1 / FPS
COLOR = ['BLUE']
# -----------------------------------------------------------------------------


def change_color(d):
    """
    Change difficulty of the game.

    :return:
    """
    COLOR[0] = d


def play_function():
    nickname = Example()
    nickname.showDialog()
    main_menu.disable()
    color2 = COLOR[0]
    map = GAME.MAP()
    if color2 == 'BLUE':
        constants.FIELD_COLOR = constants.BLUE
    elif color2 == 'WHITE':
        constants.FIELD_COLOR = constants.WHITE
    elif color2 == 'RED':
        constants.FIELD_COLOR = constants.RED
    elif color2 == 'GREEN':
        constants.FIELD_COLOR = constants.GREEN
    elif color2 == 'YELLOW':
        constants.FIELD_COLOR = constants.GOOGLE_YELLOW
    game = True
    while game:
        if main_menu.is_disabled():
            map.run(surface)
        for events in pygame.event.get():
            if events.type == pygame.KEYDOWN:
                if events.key == pygame.K_ESCAPE:
                    main_menu.enable()
                    game = False
            elif events.type == pygame.QUIT:
                game = False
    main_menu.reset(1)


def score_output():
    result = Results()
    main_menu.disable()
    main_menu.reset(1)
    game = True
    while game:
        if main_menu.is_disabled():
            result.draw(surface)
        for events in pygame.event.get():
            if events.type == pygame.KEYDOWN:
                if events.key == pygame.K_ESCAPE:
                    game = False
            elif events.type == pygame.QUIT:
                game = False
    main_menu.enable()


def main_background():
    surface.fill(COLOR_BACKGROUND)

# -----------------------------------------------------------------------------

# Меню начала игры

play_menu = pygameMenu.Menu(surface,
                            bgfun=main_background,
                            color_selected=COLOR_WHITE,
                            font=pygameMenu.fonts.FONT_BEBAS,
                            font_color=COLOR_YELLOW,
                            font_size=25,
                            menu_alpha=100,
                            menu_color=COLOR_BACKGROUND,
                            menu_height=int(WINDOW_SIZE[1] * 0.6),
                            menu_width=int(WINDOW_SIZE[0] * 0.6),
                            onclose=PYGAME_MENU_DISABLE_CLOSE,
                            option_shadow=False,
                            title='Start game',
                            window_height=WINDOW_SIZE[1],
                            window_width=WINDOW_SIZE[0]
                            )
play_menu.add_option('START', play_function)
play_menu.add_selector('color', [('Blue', 'BLUE'),
                                        ('White', 'WHITE'),
                                        ('Red', 'RED'),
                                        ('Green', 'GREEN'),
                                        ('Yellow', 'YELLOW')],
                       onreturn=None,
                       onchange=change_color)

play_menu.add_option('Return', PYGAME_MENU_BACK)

# Меню рекордов

score_menu = pygameMenu.TextMenu(surface,
                                 bgfun=main_background,
                                 color_selected=COLOR_WHITE,
                                 font=pygameMenu.fonts.FONT_BEBAS,
                                 font_color=COLOR_YELLOW,
                                 font_size=25,
                                 menu_alpha=100,
                                 font_title=pygameMenu.fonts.FONT_8BIT,
                                 menu_color=COLOR_BACKGROUND,
                                 menu_height=int(WINDOW_SIZE[1] * 0.6),
                                 menu_width=int(WINDOW_SIZE[0] * 0.6),
                                 onclose=PYGAME_MENU_DISABLE_CLOSE,
                                 option_shadow=False,
                                 text_color=COLOR_YELLOW,
                                 text_fontsize=20,
                                 title='Score',
                                 window_height=WINDOW_SIZE[1],
                                 window_width=WINDOW_SIZE[0]
                                 )
score_menu.add_option('Score', score_output)
score_menu.add_option('Return', PYGAME_MENU_BACK)

# Главное меню
main_menu = pygameMenu.Menu(surface,
                            bgfun=main_background,
                            color_selected=COLOR_WHITE,
                            font=pygameMenu.fonts.FONT_BEBAS,
                            font_color=COLOR_YELLOW,
                            font_size=25,
                            menu_alpha=100,
                            menu_color=COLOR_BACKGROUND,
                            menu_height=int(WINDOW_SIZE[1] * 0.6),
                            menu_width=int(WINDOW_SIZE[0] * 0.6),
                            onclose=PYGAME_MENU_DISABLE_CLOSE,
                            option_shadow=False,
                            title='Pacman',
                            window_height=WINDOW_SIZE[1],
                            window_width=WINDOW_SIZE[0]
                            )
main_menu.add_option('Play', play_menu)
main_menu.add_option('Score', score_menu)
main_menu.add_option('Quit', PYGAME_MENU_EXIT)

# -----------------------------------------------------------------------------
app = QApplication(sys.argv)
# Основной цикл
def start():
    while True:
        clock.tick(60)
        events = pygame.event.get()
        for event in events:
            if event.type == QUIT:
                exit()
        main_menu.mainloop(events)
        pygame.display.flip()
