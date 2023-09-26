import pygame
from random import randrange as rnd, choice
from datetime import datetime as dt

import settings
from settings import DIFF
import variables
from logger import setup_logger


log_file = 'dwall.json'
dwall_log = setup_logger('dwall_logger', log_file)


def generate_new_dwall(dblock_w, dblock_h, dwall_list_previous, difficulty):
    # 1 mark vacant places in previous dwall
    new_dwall_list = [0]*11
    zero_list = []
    for i in range(1, len(dwall_list_previous)):
        if not dwall_list_previous[i]:
            new_dwall_list[i] = i
        else:
            new_dwall_list[i] = 0
            zero_list.append(i)
    # 2 take min and max amount of zero places
    max_counter = DIFF[difficulty][1]
    min_counter = DIFF[difficulty][0]
    # 3 define amount of zero places
    counter = rnd(min_counter, max_counter+1, 1)
    # 4 define number of twins
    if difficulty in (3, 4, 5):
        twin = 1
    else:
        if counter >= 2:
            twin = choice([0, 1])
        else:
            twin = 0
    # 5 make new dwall list
    vacant = len(zero_list)
    if vacant >= counter:
        y_input = True
        if counter > 1 and twin > 0:
            pairs = []
            for i in range(vacant-1):
                if zero_list[i] + 1 == zero_list[i+1]:
                    pairs.append((zero_list[i], zero_list[i+1]))
        if twin:
            if pairs:
                x, y = choice(pairs)
                zero_list.remove(x)
                zero_list.remove(y)
                counter -= 2
            else:
                x = choice(zero_list)
                if x + 1 >= 11:
                    y = x - 1
                else:
                    y = choice(x+1, x-1)
                y_input = False
                zero_list.remove(x)
                counter -= 2
            if counter > 0:
                while counter:
                    x = choice(zero_list)
                    zero_list.remove(x)
                    counter -= 1
        else:
            while counter:
                x = choice(zero_list)
                zero_list.remove(x)
                counter -= 1
        # fill new dwall list with zero places
        for i in zero_list:
            new_dwall_list[i] = i
            if not y_input:
                new_dwall_list[y] = 0
                y_input = True
    else:
        y_input = True
        if vacant == 1:
            if twin:
                x = zero_list[0]
                if x + 1 >= 11:
                    y = x - 1
                else:
                    y = choice(x+1, x-1)
                zero_list.pop()
                y_input = False
                counter -= 2
            else:
                zero_x = zero_list[0]
                counter -= 1
                while counter:
                    x = choice(new_dwall_list)
                    if x not in (0, zero_x, zero_x+1, zero_x-1):
                        new_dwall_list[x] = 0
                        counter -= 1
                zero_list.pop()
        else:
            if counter > 1 and twin:
                pairs = []
                for i in range(vacant-1):
                    if zero_list[i] + 1 == zero_list[i+1]:
                        pairs.append((zero_list[i], zero_list[i+1]))
            if twin:
                if pairs:
                    x, y = choice(pairs)
                    zero_list.remove(x)
                    zero_list.remove(y)
                    counter -= 2
                    if counter > 0:
                        while counter:
                            x = choice(new_dwall_list)
                            zero_list.remove(x)
                            counter -= 1
                else:
                    x = choice(zero_list)
                    if x + 1 >= 11:
                        y = x - 1
                    else:
                        y = x + 1
                    y_input = False
                    zero_list.remove(x)
                    counter -= 2
            else:
                while counter:
                    x = choice(new_dwall_list)
                    zero_list.remove(x)
                    counter -= 1
        if zero_list:
            for i in zero_list:
                new_dwall_list[i] = i
                if not y_input:
                    new_dwall_list[y] = 0
                    y_input = True
        else:
            if not y_input:
                new_dwall_list[y] = 0
                y_input = True

    # LOGS
    print(new_dwall_list)
    dwall_log.info(
            {
                'time': str(dt.now()),
                'message': 'create_new_dwall',
                'dwall_list': new_dwall_list
            }
        )

    new_dwall = [pygame.Rect(70 * j - 70,
                             -70,
                             dblock_w,
                             dblock_h) for j in new_dwall_list]
    return new_dwall, new_dwall_list


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
        self.dwall_list_previous = [0, 0, 2, 0, 4, 0, 6, 0, 8, 0, 10]
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
        if self.dwall_amount != 0 and not variables.dwall_changed:
            if variables.SESSION_STAGE == 'START_TRAIN':
                if (self.dwall_amount != settings.dwall_amount and
                        self.dwall_amount % settings.dw_am_sp == 0):
                    pygame.event.post(
                        pygame.event.Event(settings.DWALL_DIFF))
            elif variables.SESSION_STAGE == 'START_EXAM':
                if (self.dwall_amount != settings.exam_dwall_amount and
                        self.dwall_amount % settings.ex_dw_am_sp == 0):
                    pygame.event.post(
                        pygame.event.Event(settings.DWALL_DIFF))

    def change_state(self):
        # SESSION STATE CHANGE
        if variables.SESSION_STAGE == 'START_TRAIN':
            variables.SESSION_STAGE = 'STOP_STAGE'
            pygame.event.post(
                pygame.event.Event(settings.STOP_STAGE))
            variables.SESSION_STAGE = 'PRE_EXAM'
            pygame.event.post(
                pygame.event.Event(settings.PRE_EXAM))
            self.dwall_amount = settings.exam_dwall_amount
            self.difficulty = settings.exam_difficulty
            self.player.health = settings.exam_health
            self.player.score = settings.exam_score
        elif variables.SESSION_STAGE == 'START_EXAM':
            variables.SESSION_STAGE = 'STOP_STAGE'
            pygame.event.post(
                pygame.event.Event(settings.STOP_STAGE))
            variables.SESSION_STAGE = 'RESULT'

    def update(self, delta_t):
        # check difficulty
        self.check_difficulty()
        # creating death wall
        if self.dwall_amount > 0:
            if len(self.dwall) == 0:
                self.dwall, self.dwall_list_previous = generate_new_dwall(
                    self.dblock_w,
                    self.dblock_h,
                    self.dwall_list_previous,
                    self.difficulty)
                variables.dwall_changed = False
        else:
            variables.score = self.player.score
            self.player.square.left = (self.app.res[0] // 2
                                       - self.player.square_w // 2)
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
                    if variables.accelerate:
                        dw_speed = variables.dwall_speed / 2
                    else:
                        dw_speed = variables.dwall_speed
                    dwall_log.info(
                        {
                            'time': str(dt.now()),
                            'message': 'death',
                            'health': self.player.health,
                            'player_pos': self.player.square.x,
                            'max_dwall_speed': dw_speed,
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
                    self.player.square.left = (self.app.res[0] // 2
                                               - self.player.square_w // 2)
                    variables.score = self.player.score
                    # LOGS
                    print('Game over')
                    if variables.accelerate:
                        dw_speed = variables.dwall_speed / 2
                    else:
                        dw_speed = variables.dwall_speed
                    dwall_log.info(
                        {
                            'time': str(dt.now()),
                            'message': 'game_over',
                            'score': variables.score,
                            'player_pos': self.player.square.x,
                            'max_dwall_speed': dw_speed,
                            'difficulty': variables.dwall_difficulty
                        }
                    )
                    self.change_state()
                    break
