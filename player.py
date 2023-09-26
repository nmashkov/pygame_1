import pygame
from datetime import datetime as dt

import settings
import variables
from logger import setup_logger


log_file = 'player.json'
player_log = setup_logger('player_logger', log_file)

log_file = 'player_pos.json'
player_pos_log = setup_logger('player_pos_logger', log_file)


class Player(pygame.sprite.Sprite):
    def __init__(self, app):
        pygame.sprite.Sprite.__init__(self)
        self.app = app
        group = self.app.all_sprites
        self.add(group)
        # square params
        self.square_color = settings.square_color
        self.square_w = settings.square_w
        self.square_h = settings.square_h
        self.square_speed = settings.square_speed
        #
        self.image = pygame.Surface((self.square_w, self.square_h))
        self.image.fill(self.square_color)
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.app.res[0] // 2 - self.square_w // 2,
                             self.app.res[1] - self.square_h - 10)
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

    def log_player_pos(self):
        if variables.pl_pos_log and variables.is_warmuped:
            player_pos_log.info(
                {
                    'time': f'{dt.now()}',
                    'player_pos': self.rect.x
                }
            )
            variables.pl_pos_log = False

    def update(self, delta_t=1/60):
        # player controls
        key = pygame.key.get_pressed()
        if variables.SESSION_STAGE in ('START_TRAIN', 'START_EXAM'):
            # move left
            # LP
            if key[self.left_button_1] and self.rect.left > 5:
                self.rect.x -= self.square_speed * delta_t
            # RP
            if key[self.left_button_2] and self.rect.left > 5:
                self.rect.x -= self.square_speed * delta_t
            # move right
            # LP
            if (key[self.right_button_1] and
                    self.rect.right < self.app.res[0]-5):
                self.rect.x += self.square_speed * delta_t
            # RP
            if (key[self.right_button_2] and
                    self.rect.right < self.app.res[0]-5):
                self.rect.x += self.square_speed * delta_t
            # accelerate death wall
            if key[self.acc_button_1] or key[self.acc_button_2]:
                variables.dwall_speed = variables.acc_dwall_speed
            else:
                variables.dwall_speed = variables.acc_dwall_speed / 2
