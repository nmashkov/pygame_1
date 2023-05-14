import uuid
import pathlib

import pygame


# main game settings
NAME = 'Игра 1'
WIDTH, HEIGHT = 700, 900
FPS = 60
bg_color = (239, 239, 239)

# log folder settings
BASE_DIR = str(pathlib.Path().resolve())
BASE_LOGS_DIR = 'logs'
SESSION_DIR = str(uuid.uuid1())

# EVENTS
START_MENU = pygame.USEREVENT + 1
START_TRAIN = pygame.USEREVENT + 2
PRE_EXAM = pygame.USEREVENT + 3
START_EXAM = pygame.USEREVENT + 4
STOP_STAGE = pygame.USEREVENT + 5
RESULT = pygame.USEREVENT + 6
PLAYER_POS = pygame.USEREVENT + 7
DWALL_DIFF = pygame.USEREVENT + 8

# colors
accent = (41, 166, 236)
back1 = (51, 128, 243)
back1_hover = (27, 87, 177)
back2 = (184, 209, 246)
dark_grey = (51, 51, 51)
light_grey = (112, 112, 112)
light_grey2 = (215, 215, 215)
accent2 = (88, 165, 27)

# player square settings
square_color = (136, 37, 215)
square_w = 50
square_h = 50
square_speed = 3
PLPOSLOG_TIMER = 100

# player controls
LEFT_1 = pygame.K_a
RIGHT_1 = pygame.K_d
ACCELERATE_1 = pygame.K_s
START_1 = pygame.K_w
LEFT_2 = pygame.K_LEFT
RIGHT_2 = pygame.K_RIGHT
ACCELERATE_2 = pygame.K_DOWN
START_2 = pygame.K_UP
EXIT = pygame.K_ESCAPE
CONTINUE = pygame.K_RETURN

# death wall settings
dblock_w = 70
dblock_h = 70
dblock_color = (219, 59, 59)

warmup_time = 3

# train player and stats settings
dwall_speed = 4
dwall_amount = 30
health = 3
score = 0
difficulty = 5  # 2 < d < 6 = 3, 4, 5

# train difficulty step values
dw_sp_step = 0.5
dw_am_sp = 5

# exam player and stats settings
exam_dwall_speed = 5
exam_dwall_amount = 50
exam_health = 3
exam_score = 0
exam_difficulty = 5  # 2 < d < 6 = 3, 4, 5

# exam difficulty step values
ex_dw_sp_step = 0.5
ex_dw_am_sp = 5
ex_dw_am_dif_1 = 40
ex_dw_am_dif_2 = 25
ex_dw_dif_step = 1
