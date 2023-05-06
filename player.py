import pygame

import settings
import variables
from logger import setup_logger


log_file = 'player.json'
player_log = setup_logger('player_logger', log_file)


def pause(app):
    paused = True
    while paused:
        [exit() for i in pygame.event.get() if i.type == pygame.QUIT]

        key = pygame.key.get_pressed()
        if key[pygame.K_RETURN]:
            paused = False

        # pygame.display.update()
        app.clock.tick(15)


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

    def update(self, delta_t=1/60):
        # player controls
        key = pygame.key.get_pressed()
        if variables.SESSION_STAGE not in ('START_MENU', 'STOP_STAGE'):
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
                self.app.dwall.dwall_speed = settings.dwall_speed * 2
            else:
                self.app.dwall.dwall_speed = settings.dwall_speed
            # pause game
            if key[pygame.K_p]:
                pause(self.app)
        # exit app
        if key[self.exit_button]:
            pygame.event.post(self.app.quit_event)
