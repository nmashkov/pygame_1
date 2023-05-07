import uuid
import pathlib

import pygame


# main game settings
NAME = 'Game 1'
WIDTH, HEIGHT = 700, 900
FPS = 60
bg_color = (190, 190, 190)

# log folder settings
BASE_DIR = str(pathlib.Path().resolve())
BASE_LOGS_DIR = 'logs'
SESSION_DIR = str(uuid.uuid1())

# player square settings
square_color = (136, 39, 255)
square_w = 50
square_h = 50
square_speed = 3
PLPOSLOG_TIMER = 100

# player controls
LEFT_1 = pygame.K_a
RIGHT_1 = pygame.K_d
ACCELERATE_1 = pygame.K_s
LEFT_2 = pygame.K_LEFT
RIGHT_2 = pygame.K_RIGHT
ACCELERATE_2 = pygame.K_DOWN
EXIT = pygame.K_ESCAPE

# death wall settings
dblock_w = 70
dblock_h = 70
dblock_color = (255, 107, 107)
dwall_speed = 4

# train player and stats settings
dwall_amount = 30
health = 3
score = 0
difficulty = 5  # 2 < d < 6 = 3, 4, 5

# exam player and stats settings
exam_dwall_amount = 60
exam_health = 3
exam_score = 0
