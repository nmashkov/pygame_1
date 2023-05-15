import pygame
from datetime import datetime as dt

import settings
import variables
from logger import setup_logger


log_file = 'player.json'
player_log = setup_logger('player_logger', log_file)

log_file = 'player_pos.json'
player_pos_log = setup_logger('player_pos_logger', log_file)


class Player:
    def __init__(self, app):
        self.app = app
        # square params
        self.square_color = settings.square_color
        self.square_w = settings.square_w
        self.square_h = settings.square_h
        self.square_speed = settings.square_speed
        self.square = pygame.Rect(self.app.res[0] // 2 - self.square_w // 2,
                                  self.app.res[1] - self.square_h - 10,
                                  self.square_w,
                                  self.square_h)
        # controls
        self.left_button_1 = settings.LEFT_1
        self.right_button_1 = settings.RIGHT_1
        self.acc_button_1 = settings.ACCELERATE_1
        self.left_button_2 = settings.LEFT_2
        self.right_button_2 = settings.RIGHT_2
        self.acc_button_2 = settings.ACCELERATE_2
        self.exit_button = settings.EXIT
        # stats
        self.health = settings.health
        self.score = settings.score

    def draw(self):
        # drawing player square
        pygame.draw.rect(self.app.screen, self.square_color, self.square)

    def log_player_pos(self):
        if variables.pl_pos_log:
            player_pos_log.info(
                {
                    'time': f'{dt.now()}',
                    'player_pos': self.square.x
                }
            )
            variables.pl_pos_log = False

    def update(self, delta_t=1/60):
        # player controls
        key = pygame.key.get_pressed()
        if variables.SESSION_STAGE in ('START_TRAIN', 'START_EXAM'):
            # move left
            # LP
            if key[self.left_button_1] and self.square.left > 5:
                self.square.left -= self.square_speed * delta_t
            # RP
            if key[self.left_button_2] and self.square.left > 5:
                self.square.left -= self.square_speed * delta_t
            # move right
            # LP
            if (key[self.right_button_1] and
                    self.square.right < self.app.res[0]-5):
                self.square.right += self.square_speed * delta_t
            # RP
            if (key[self.right_button_2] and
                    self.square.right < self.app.res[0]-5):
                self.square.right += self.square_speed * delta_t
            # accelerate death wall
            if key[self.acc_button_1] or key[self.acc_button_2]:
                variables.dwall_speed = variables.acc_dwall_speed
            else:
                variables.dwall_speed = variables.acc_dwall_speed / 2

        # exit app
        if key[self.exit_button]:
            pygame.event.post(self.app.quit_event)
