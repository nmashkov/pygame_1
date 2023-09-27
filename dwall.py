import pygame
from random import randrange as rnd, choice
from datetime import datetime as dt

import settings
from settings import DIFF
import variables
from logger import setup_logger


log_file = 'dwall.json'
dwall_log = setup_logger('dwall_logger', log_file)


def generate_new_dwall(dwall_list_previous, difficulty):
    print('=the first dwall generator=')
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
                    y = choice([x+1, x-1])
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
                    y = choice([x+1, x-1])
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
    print(f'new_dwall_list= {new_dwall_list}')
    print('==================================================')
    dwall_log.info(
            {
                'time': str(dt.now()),
                'message': 'create_new_dwall',
                'dwall_list': new_dwall_list
            }
        )
    return new_dwall_list


def generate_new_dwall_alternate(dwall_list_previous, difficulty):
    print('=the alternate dwall generator=')
    # 1 mark vacant places in previous dwall
    new_dwall_list = [0]*11
    fill_list = []
    zero_list = []
    segments = []
    k = 0
    max_segment = [0, 0]
    max_segments = []
    for i in range(1, len(dwall_list_previous)):
        if not dwall_list_previous[i]:
            new_dwall_list[i] = i
            if k > 0:
                if k > max_segment[0]:
                    max_segment[0] = k
                    max_segment[1] = i-k
                    max_segments = []
                    max_segments.append((k, i-k))
                elif k == max_segment[0]:
                    max_segments.append((k, i-k))
                segments.append((k, i-k))
                k = 0
        else:
            k += 1
            new_dwall_list[i] = 0
            fill_list.append(i)
    if k > 0:
        if k > max_segment[0]:
            max_segment[0] = k
            max_segment[1] = i-k+1
        elif k == max_segment[0]:
            max_segments.append((k, i-k+1))
        segments.append((k, i-k+1))
        k = 0
    # 3 make new dwall list
    # if diff=1, simple rnd choice
    if difficulty == 1:
        x = choice(fill_list)
        fill_list.remove(x)
    elif difficulty == 2:
        x = choice(fill_list)
        fill_list.remove(x)
        up_list = []
        if x-1 in fill_list:
            fill_list.remove(x-1)
            up_list.append(x-1)
        if x+1 in fill_list:
            fill_list.remove(x+1)
            up_list.append(x+1)
        x = choice(fill_list)
        fill_list.remove(x)
        if up_list:
            for i in up_list:
                fill_list.append(i)
    else:
        up_list = []
        difficulty -= 1
        if len(max_segments) > 1:
            segment = choice(max_segments)
        else:
            segment = max_segment
        if segment[0] == difficulty:
            first_index = segment[1]
            last_index = first_index + segment[0]
            for i in range(first_index, last_index):
                fill_list.remove(i)
            if first_index-1 in fill_list:
                fill_list.remove(first_index-1)
                up_list.append(first_index-1)
            if last_index in fill_list:
                fill_list.remove(last_index)
                up_list.append(last_index)
        elif segment[0] > difficulty:
            k = segment[0] - difficulty
            first_index = segment[1]
            last_index = segment[1] + k
            choice_index = rnd(first_index, last_index+1, 1)
            last_index = choice_index + difficulty
            for i in range(choice_index, last_index):
                fill_list.remove(i)
            if choice_index-1 in fill_list:
                fill_list.remove(choice_index-1)
                up_list.append(choice_index-1)
            if last_index in fill_list:
                fill_list.remove(last_index)
                up_list.append(last_index)
        else:
            k = difficulty - segment[0]
            first_index = segment[1]
            last_index = first_index + segment[0]
            while k:
                if last_index + 1 > 11:
                    first_index -= k
                    break
                else:
                    last_index += 1
                    k -= 1
                if first_index - 1 < 1:
                    last_index += k
                    break
                else:
                    first_index -= 1
                    k -= 1
            for i in range(first_index, last_index):
                if i in fill_list:
                    fill_list.remove(i)
                else:
                    zero_list.append(i)
        # last block
        if fill_list:
            x = choice(fill_list)
            fill_list.remove(x)
        else:
            new_list = []
            for i in new_dwall_list:
                if i:
                    new_list.append(i)
            x = choice(new_list)
            new_dwall_list[x] = 0
        if up_list:
            for i in up_list:
                fill_list.append(i)
    # fill other places with blocks
    for i in fill_list:
        new_dwall_list[i] = i
    if zero_list:
        for i in zero_list:
            new_dwall_list[i] = 0
    print(f'new_dwall_list= {new_dwall_list}')
    print('==================================================')
    return new_dwall_list


class DwallBlockSprite(pygame.sprite.Sprite):
    def __init__(self, dwall, x, y, group, player):
        pygame.sprite.Sprite.__init__(self)
        self.add(group)
        self.player = player
        self.dwall = dwall
        # dblock params
        self.dblock_w = settings.dblock_w
        self.dblock_h = settings.dblock_h
        self.dblock_color = settings.dblock_color
        # dblock construct
        self.image = pygame.Surface((self.dblock_w, self.dblock_h))
        self.image.fill(self.dblock_color)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def check_player_collision(self):
        if self.rect.colliderect(self.player.rect):
            variables.dead = True
            for dblock in self.dwall:
                dblock.kill()

    def update(self):
        # dwall moving
        self.rect.move_ip(0, variables.dwall_speed)
        # check collision with player
        self.check_player_collision()
        # dwall check end of runway
        if self.rect.top > settings.HEIGHT:
            self.kill()
            variables.passed = True


class DwallGroup(pygame.sprite.Group):
    def __init__(self, app):
        super().__init__()
        self.app = app

    def check_passing_or_dead(self):
        if variables.passed:
            variables.passed = False
            variables.dwall_amount -= 1
            self.app.player.score += 1
            # LOGS
            print(f'points: {self.app.player.score}')
            dwall_log.info(
                {
                    'time': str(dt.now()),
                    'message': 'update_score',
                    'score': self.app.player.score
                }
            )
        elif variables.dead:
            variables.dead = False
            self.app.player.rect.topleft = (
                settings.WIDTH // 2 - self.app.player.square_w // 2,
                settings.HEIGHT - self.app.player.square_h - 10
            )
            if self.app.player.health > 1:
                variables.dwall_amount -= 1
                self.app.player.health -= 1
                # LOGS
                print(f'Death. Remains {self.app.player.health} attempts')
                if variables.accelerate:
                    dw_speed = variables.dwall_speed / 2
                else:
                    dw_speed = variables.dwall_speed
                dwall_log.info(
                    {
                        'time': str(dt.now()),
                        'message': 'death',
                        'health': self.app.player.health,
                        'player_pos': self.app.player.rect.x,
                        'max_dwall_speed': dw_speed,
                        'difficulty': variables.dwall_difficulty
                    }
                )
            else:
                self.app.player.health -= 1
                variables.score = self.app.player.score
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
                        'player_pos': self.app.player.rect.x,
                        'max_dwall_speed': dw_speed,
                        'difficulty': variables.dwall_difficulty
                    }
                )
                self.change_state()

    def CheckEmpty(self):
        sprites = self.sprites()
        if not sprites:
            if variables.dwall_amount > 0:
                dwall_list = generate_new_dwall(variables.dwall_list_previous,
                                                variables.dwall_difficulty)
                # dwall_list = generate_new_dwall_alternate(
                #     variables.dwall_list_previous,
                #     variables.dwall_difficulty)
                # variables.dwall_list_previous = dwall_list
                variables.dwall_changed = False
                for j in dwall_list:
                    self.add(DwallBlockSprite(self,
                                              70 * j-35,
                                              -35,
                                              self.app.all_sprites,
                                              self.app.player))
            else:
                variables.score = self.app.player.score
                self.app.player.rect.topleft = (
                    settings.WIDTH // 2 - self.app.player.square_w // 2,
                    settings.HEIGHT - self.app.player.square_h - 10
                )
                self.change_state()

    def check_difficulty(self):
        if variables.dwall_amount != 0 and not variables.dwall_changed:
            if variables.SESSION_STAGE == 'START_TRAIN':
                if (variables.dwall_amount != settings.dwall_amount and
                        variables.dwall_amount % settings.dw_am_sp == 0):
                    pygame.event.post(
                        pygame.event.Event(settings.DWALL_DIFF))
            elif variables.SESSION_STAGE == 'START_EXAM':
                if (variables.dwall_amount != settings.exam_dwall_amount and
                        variables.dwall_amount % settings.ex_dw_am_sp == 0):
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
            variables.dwall_amount = settings.exam_dwall_amount
            variables.dwall_difficulty = settings.exam_difficulty
            self.app.player.health = settings.exam_health
            self.app.player.score = settings.exam_score
        elif variables.SESSION_STAGE == 'START_EXAM':
            variables.SESSION_STAGE = 'STOP_STAGE'
            pygame.event.post(
                pygame.event.Event(settings.STOP_STAGE))
            variables.SESSION_STAGE = 'RESULT'

    def update(self):
        self.check_difficulty()
        self.CheckEmpty()
        super().update()
        self.check_passing_or_dead()
