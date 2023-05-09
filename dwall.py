import pygame
from random import randrange as rnd
from datetime import datetime as dt

import settings
import variables
import event_manager
from logger import setup_logger


log_file = 'dwall.json'
dwall_log = setup_logger('dwall_logger', log_file)


def dwall_new(dblock_w, dblock_h, dwall_list_previous, difficulty):
    done = False
    while not done:
        dwall_list = [i*rnd(0, 2) for i in range(11)]

        for i in range(1, len(dwall_list_previous)):
            if not dwall_list_previous[i]:
                dwall_list[i] = i

        if dwall_list == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
            dwall_list = [0, 0, 2, 3, 4, 5, 6, 7, 8, 9, 0]
        if dwall_list == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]:
            dwall_list = [0, 1, 0, 3, 4, 5, 6, 7, 8, 0, 10]

        counter = 0
        for i in dwall_list:
            if not i:
                counter += 1
        if counter < difficulty:
            done = True

    # LOGS
    print(dwall_list)
    dwall_log.info(
            {
                'time': str(dt.now()),
                'message': 'create_new_dwall',
                'dwall_list': dwall_list
            }
        )

    new_dwall = [pygame.Rect(70 * j - 70,
                             -70,
                             dblock_w,
                             dblock_h) for j in dwall_list]
    return new_dwall, dwall_list


class Dwall:
    def __init__(self, app):
        self.app = app
        self.player = self.app.player
        # dwall params
        self.dblock_w = settings.dblock_w
        self.dblock_h = settings.dblock_h
        self.dblock_color = settings.dblock_color
        self.dwall_speed = settings.dwall_speed
        # dwall utils
        self.dwall = []
        self.dwall_list_previous = []
        self.difficulty = settings.difficulty
        self.dwall_amount = settings.dwall_amount

    def draw(self):
        # drawing death wall
        [pygame.draw.rect(self.app.screen, self.dblock_color, dblock)
         for dblock in self.dwall]

    def check_difficulty(self):
        variables.dwall_amount = self.dwall_amount
        self.dwall_speed = variables.dwall_speed
        self.difficulty = variables.dwall_difficulty
        if self.dwall_amount != 0:
            if variables.SESSION_STAGE == 'START_TRAIN':
                if (not variables.dwall_changed and
                        self.dwall_amount != settings.dwall_amount and
                        self.dwall_amount % settings.dw_am_sp == 0):
                    pygame.event.post(
                        pygame.event.Event(event_manager.DWALL_DIFF))
                    dwall_log.info(
                        {
                            'time': f'{dt.now()}',
                            'message': 'DIFFICULTY_UP',
                            'dwall_amount': variables.dwall_amount
                        }
                    )
            elif variables.SESSION_STAGE == 'START_EXAM':
                if (not variables.dwall_changed and
                        self.dwall_amount != settings.exam_dwall_amount and
                        self.dwall_amount % settings.ex_dw_am_sp == 0):
                    pygame.event.post(
                        pygame.event.Event(event_manager.DWALL_DIFF))
                    dwall_log.info(
                        {
                            'time': f'{dt.now()}',
                            'message': 'DIFFICULTY_UP',
                            'dwall_amount': variables.dwall_amount
                        }
                    )

    def change_state(self):
        # SESSION STATE CHANGE
        if variables.SESSION_STAGE == 'START_TRAIN':
            variables.SESSION_STAGE = 'STOP_STAGE'
            pygame.event.post(
                pygame.event.Event(event_manager.STOP_STAGE))
            variables.SESSION_STAGE = 'PRE_EXAM'
            pygame.event.post(
                pygame.event.Event(event_manager.PRE_EXAM))
            self.dwall_amount = settings.exam_dwall_amount
            self.difficulty = settings.exam_difficulty
            self.player.health = settings.exam_health
            self.player.score = settings.exam_score
        elif variables.SESSION_STAGE == 'START_EXAM':
            variables.SESSION_STAGE = 'STOP_STAGE'
            pygame.event.post(
                pygame.event.Event(event_manager.STOP_STAGE))
            variables.SESSION_STAGE = 'RESULT'

    def update(self, delta_t):
        # check difficulty
        self.check_difficulty()
        # creating death wall
        if self.dwall_amount > 0:
            if len(self.dwall) == 0:
                self.dwall, self.dwall_list_previous = dwall_new(
                    self.dblock_w,
                    self.dblock_h,
                    self.dwall_list_previous,
                    self.difficulty)
                variables.dwall_changed = False
        else:
            variables.score = self.player.score
            self.change_state()

        # drawing checkline
        line = pygame.draw.line(self.app.screen,
                                (255, 255, 255),
                                [0, self.app.res[1]],
                                [self.app.res[0], self.app.res[1]],
                                3)

        # death wall moving and checks
        for dblock in self.dwall:
            dblock.y += self.dwall_speed * delta_t
            # collision with line
            collision_with_line = line.collidelistall(self.dwall)
            if len(collision_with_line) > 0:
                self.dwall = []
                self.dwall_amount -= 1
                self.player.score += 1
                # LOGS
                print(f'points: {self.player.score}')
                dwall_log.info(
                    {
                        'time': str(dt.now()),
                        'message': 'update_score',
                        'score': self.player.score
                    }
                )
                break
            # collision with player
            collisions = self.player.square.collidelistall(self.dwall)
            if len(collisions) > 0:
                if self.player.health > 1:
                    self.dwall_amount -= 1
                    self.player.health -= 1
                    # LOGS
                    print(f'Death. Remains {self.player.health} attempts')
                    dwall_log.info(
                        {
                            'time': str(dt.now()),
                            'message': 'death',
                            'health': self.player.health,
                            'player_pos': self.player.square.x,
                            'max_dwall_speed': variables.dwall_speed,
                            'difficulty': variables.dwall_difficulty
                        }
                    )
                    self.dwall = []
                    self.player.square.left = (self.app.res[0] // 2
                                               - self.player.square_w // 2)
                    break
                else:
                    self.player.health -= 1
                    self.dwall = []
                    variables.score = self.player.score
                    # LOGS
                    print('Game over')
                    dwall_log.info(
                        {
                            'time': str(dt.now()),
                            'message': 'game_over',
                            'score': variables.score,
                            'player_pos': self.player.square.x,
                            'max_dwall_speed': variables.dwall_speed,
                            'difficulty': variables.dwall_difficulty
                        }
                    )
                    self.change_state()
