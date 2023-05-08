import sys
import pygame
from datetime import datetime as dt, timedelta as td

import settings
import variables
from logger import setup_logger
from player import player_log, player_pos_log


log_file = 'events.json'
event_log = setup_logger('event_logger', log_file)


START_MENU = pygame.USEREVENT + 1
START_TRAIN = pygame.USEREVENT + 2
PRE_EXAM = pygame.USEREVENT + 3
START_EXAM = pygame.USEREVENT + 4
STOP_STAGE = pygame.USEREVENT + 5
RESULT = pygame.USEREVENT + 6
PLAYER_POS = pygame.USEREVENT + 7
DWALL_DIFF = pygame.USEREVENT + 8


def player_events(events):
    key = pygame.key.get_pressed()

    variables.cooperation = (
        (key[settings.LEFT_1] and key[settings.LEFT_2]) and
        not (key[settings.RIGHT_1] or key[settings.RIGHT_2])
        or
        not (key[settings.LEFT_1] or key[settings.LEFT_2]) and
        (key[settings.RIGHT_1] and key[settings.RIGHT_2])
    )

    variables.conflict = (
        (key[settings.LEFT_1] and key[settings.RIGHT_2])
        or
        (key[settings.RIGHT_1] and key[settings.LEFT_2])
    )

    variables.accelerate = (
        key[settings.ACCELERATE_1] or key[settings.ACCELERATE_2]
    )

    # PLAYER CONTROL SECTION
    # KEYDOWN
    if events.type == pygame.KEYDOWN:
        # LP
        if events.key == settings.LEFT_1:
            variables.lp_key_pushes += 1
            variables.lp_left_time = dt.now()
            player_log.info(
                {
                    'time': str(dt.now()),
                    'message': 'LP_LEFT_DOWN'
                }
            )
            if variables.cooperation:
                if not variables.coop_started:
                    variables.coop_started = True
                    variables.start_cooperative_time = dt.now()
                    player_log.info(
                        {
                            'time': str(dt.now()),
                            'message': 'COOP_START'
                        }
                    )
            if variables.conflict:
                if not variables.conflict_started:
                    # stop coop due to conflict
                    if variables.coop_started:
                        variables.coop_started = False
                        variables.cooperative_time += (
                            dt.now() - variables.start_cooperative_time)
                        player_log.info(
                            {
                                'time': str(dt.now()),
                                'message': 'COOP_END',
                                'cooperation_time': str(
                                    variables.cooperative_time.seconds)
                            }
                        )
                    # start conflict on click
                    variables.conflict_started = True
                    variables.start_conflict_time = dt.now()
                    player_log.info(
                        {
                            'time': str(dt.now()),
                            'message': 'CONFLICT_START'
                        }
                    )
        if events.key == settings.RIGHT_1:
            variables.lp_key_pushes += 1
            variables.lp_right_time = dt.now()
            player_log.info(
                {
                    'time': str(dt.now()),
                    'message': 'LP_RIGHT_DOWN'
                }
            )
            if variables.cooperation:
                if not variables.coop_started:
                    variables.coop_started = True
                    variables.start_cooperative_time = dt.now()
                    player_log.info(
                        {
                            'time': str(dt.now()),
                            'message': 'COOP_START'
                        }
                    )
            if variables.conflict:
                if not variables.conflict_started:
                    # stop coop due to conflict
                    if variables.coop_started:
                        variables.coop_started = False
                        variables.cooperative_time += (
                            dt.now() - variables.start_cooperative_time)
                        player_log.info(
                            {
                                'time': str(dt.now()),
                                'message': 'COOP_END',
                                'cooperation_time': str(
                                    variables.cooperative_time.seconds)
                            }
                        )
                    # start conflict on click
                    variables.conflict_started = True
                    variables.start_conflict_time = dt.now()
                    player_log.info(
                        {
                            'time': str(dt.now()),
                            'message': 'CONFLICT_START'
                        }
                    )
        if events.key == settings.ACCELERATE_1:
            variables.lp_key_pushes += 1
            variables.lp_accelerate_time = dt.now()
            player_log.info(
                {
                    'time': str(dt.now()),
                    'message': 'LP_ACCELERATE_DOWN'
                }
            )
            if variables.accelerate:
                if not variables.accelerate_started:
                    variables.accelerate_started = True
                    variables.start_accelerate_time = dt.now()
                    player_log.info(
                        {
                            'time': str(dt.now()),
                            'message': 'ACC_START'
                        }
                    )
        # RP
        if events.key == settings.LEFT_2:
            variables.rp_key_pushes += 1
            variables.rp_left_time = dt.now()
            player_log.info(
                {
                    'time': str(dt.now()),
                    'message': 'RP_LEFT_DOWN'
                }
            )
            if variables.cooperation:
                if not variables.coop_started:
                    variables.coop_started = True
                    variables.start_cooperative_time = dt.now()
                    player_log.info(
                        {
                            'time': str(dt.now()),
                            'message': 'COOP_START'
                        }
                    )
            if variables.conflict:
                if not variables.conflict_started:
                    # stop coop due to conflict
                    if variables.coop_started:
                        variables.coop_started = False
                        variables.cooperative_time += (
                            dt.now() - variables.start_cooperative_time)
                        player_log.info(
                            {
                                'time': str(dt.now()),
                                'message': 'COOP_END',
                                'cooperation_time': str(
                                    variables.cooperative_time.seconds)
                            }
                        )
                    # start conflict on click
                    variables.conflict_started = True
                    variables.start_conflict_time = dt.now()
                    player_log.info(
                        {
                            'time': str(dt.now()),
                            'message': 'CONFLICT_START'
                        }
                    )
        if events.key == settings.RIGHT_2:
            variables.rp_key_pushes += 1
            variables.rp_right_time = dt.now()
            player_log.info(
                {
                    'time': str(dt.now()),
                    'message': 'RP_RIGHT_DOWN'
                }
            )
            if variables.cooperation:
                if not variables.coop_started:
                    variables.coop_started = True
                    variables.start_cooperative_time = dt.now()
                    player_log.info(
                        {
                            'time': str(dt.now()),
                            'message': 'COOP_START'
                        }
                    )
            if variables.conflict:
                if not variables.conflict_started:
                    # stop coop due to conflict
                    if variables.coop_started:
                        variables.coop_started = False
                        variables.cooperative_time += (
                            dt.now() - variables.start_cooperative_time)
                        player_log.info(
                            {
                                'time': str(dt.now()),
                                'message': 'COOP_END',
                                'cooperation_time': str(
                                    variables.cooperative_time.seconds)
                            }
                        )
                    # start conflict on click
                    variables.conflict_started = True
                    variables.start_conflict_time = dt.now()
                    player_log.info(
                        {
                            'time': str(dt.now()),
                            'message': 'CONFLICT_START'
                        }
                    )
        if events.key == settings.ACCELERATE_2:
            variables.rp_key_pushes += 1
            variables.rp_accelerate_time = dt.now()
            player_log.info(
                {
                    'time': str(dt.now()),
                    'message': 'RP_ACCELERATE_DOWN'
                }
            )
            if variables.accelerate:
                if not variables.accelerate_started:
                    variables.accelerate_started = True
                    variables.start_accelerate_time = dt.now()
                    player_log.info(
                        {
                            'time': str(dt.now()),
                            'message': 'ACC_START'
                        }
                    )
    # KEYUP
    if events.type == pygame.KEYUP:
        # LP
        if events.key == settings.LEFT_1:
            new_date = dt.now() - variables.lp_left_time
            variables.lp_active_time += new_date
            player_log.info(
                {
                    'time': str(dt.now()),
                    'message': 'LP_LEFT_UP',
                    'time_pushed': str(new_date)
                }
            )
            if variables.coop_started:
                if not variables.cooperation:
                    variables.coop_started = False
                    variables.cooperative_time += (
                        dt.now() - variables.start_cooperative_time)
                    player_log.info(
                        {
                            'time': str(dt.now()),
                            'message': 'COOP_END',
                            'cooperation_time': str(
                                variables.cooperative_time.seconds)
                        }
                    )
            if variables.conflict_started:
                if not variables.conflict:
                    variables.conflict_started = False
                    variables.conflict_time += (
                        dt.now() - variables.start_conflict_time)
                    player_log.info(
                        {
                            'time': str(dt.now()),
                            'message': 'CONFLICT_END',
                            'conflict_time': str(
                                variables.conflict_time.seconds)
                        }
                    )
        if events.key == settings.RIGHT_1:
            new_date = dt.now() - variables.lp_right_time
            variables.lp_active_time += new_date
            player_log.info(
                {
                    'time': str(dt.now()),
                    'message': 'LP_RIGHT_UP',
                    'time_pushed': str(new_date)
                }
            )
            if variables.coop_started:
                if not variables.cooperation:
                    variables.coop_started = False
                    variables.cooperative_time += (
                        dt.now() - variables.start_cooperative_time)
                    player_log.info(
                        {
                            'time': str(dt.now()),
                            'message': 'COOP_END',
                            'cooperation_time': str(
                                variables.cooperative_time.seconds)
                        }
                    )
            if variables.conflict_started:
                if not variables.conflict:
                    variables.conflict_started = False
                    variables.conflict_time += (
                        dt.now() - variables.start_conflict_time)
                    player_log.info(
                        {
                            'time': str(dt.now()),
                            'message': 'CONFLICT_END',
                            'conflict_time': str(
                                variables.conflict_time.seconds)
                        }
                    )
        if events.key == settings.ACCELERATE_1:
            new_date = dt.now() - variables.lp_accelerate_time
            variables.lp_active_acc_time += new_date
            player_log.info(
                {
                    'time': str(dt.now()),
                    'message': 'LP_ACCELERATE_UP',
                    'time_pushed': str(new_date)
                }
            )
            if variables.accelerate_started:
                if not variables.accelerate:
                    variables.accelerate_started = False
                    variables.accelerate_time += (
                        dt.now() - variables.start_accelerate_time)
                    player_log.info(
                        {
                            'time': str(dt.now()),
                            'message': 'ACC_END',
                            'accelerate_time': str(
                                variables.accelerate_time.seconds)
                        }
                    )
        # RP
        if events.key == settings.LEFT_2:
            new_date = dt.now() - variables.rp_left_time
            variables.rp_active_time += new_date
            player_log.info(
                {
                    'time': str(dt.now()),
                    'message': 'RP_LEFT_UP',
                    'time_pushed': str(new_date)
                }
            )
            if variables.coop_started:
                if not variables.cooperation:
                    variables.coop_started = False
                    variables.cooperative_time += (
                        dt.now() - variables.start_cooperative_time)
                    player_log.info(
                        {
                            'time': str(dt.now()),
                            'message': 'COOP_END',
                            'cooperation_time': str(
                                variables.cooperative_time.seconds)
                        }
                    )
            if variables.conflict_started:
                if not variables.conflict:
                    variables.conflict_started = False
                    variables.conflict_time += (
                        dt.now() - variables.start_conflict_time)
                    player_log.info(
                        {
                            'time': str(dt.now()),
                            'message': 'CONFLICT_END',
                            'conflict_time': str(
                                variables.conflict_time.seconds)
                        }
                    )
        if events.key == settings.RIGHT_2:
            new_date = dt.now() - variables.rp_right_time
            variables.rp_active_time += new_date
            player_log.info(
                {
                    'time': str(dt.now()),
                    'message': 'RP_RIGHT_UP',
                    'time_pushed': str(new_date)
                }
            )
            if variables.coop_started:
                if not variables.cooperation:
                    variables.coop_started = False
                    variables.cooperative_time += (
                        dt.now() - variables.start_cooperative_time)
                    player_log.info(
                        {
                            'time': str(dt.now()),
                            'message': 'COOP_END',
                            'cooperation_time': str(
                                variables.cooperative_time.seconds)
                        }
                    )
            if variables.conflict_started:
                if not variables.conflict:
                    variables.conflict_started = False
                    variables.conflict_time += (
                        dt.now() - variables.start_conflict_time)
                    player_log.info(
                        {
                            'time': str(dt.now()),
                            'message': 'CONFLICT_END',
                            'conflict_time': str(
                                variables.conflict_time.seconds)
                        }
                    )
        if events.key == settings.ACCELERATE_2:
            new_date = dt.now() - variables.rp_accelerate_time
            variables.rp_active_acc_time += new_date
            player_log.info(
                {
                    'time': str(dt.now()),
                    'message': 'RP_ACCELERATE_UP',
                    'time_pushed': str(new_date)
                }
            )
            if variables.accelerate_started:
                if not variables.accelerate:
                    variables.accelerate_started = False
                    variables.accelerate_time += (
                        dt.now() - variables.start_accelerate_time)
                    player_log.info(
                        {
                            'time': str(dt.now()),
                            'message': 'ACC_END',
                            'accelerate_time': str(
                                variables.accelerate_time.seconds)
                        }
                    )


def event_handler():
    for events in pygame.event.get():
        # EVENTS SECTION
        # START MENU
        if events.type == START_MENU:
            event_log.info(
                {
                    'time': f'{dt.now()}',
                    'message': 'START_MENU',
                    'SESSION': f'{settings.SESSION_DIR}'
                }
            )
        # START TRAIN STATE
        if events.type == START_TRAIN:
            variables.pl_pos_log = True
            pygame.time.set_timer(PLAYER_POS, settings.PLPOSLOG_TIMER)
            variables.start_stage_time = dt.now()
            event_log.info(
                {
                    'time': f'{dt.now()}',
                    'message': 'START_TRAIN'
                }
            )
            player_log.info(
                {
                    'time': f'{dt.now()}',
                    'message': 'START_TRAIN'
                }
            )
            player_pos_log.info(
                {
                    'time': f'{dt.now()}',
                    'message': 'START_TRAIN'
                }
            )
        # PRE EXAM STATE
        if events.type == PRE_EXAM:
            event_log.info(
                {
                    'time': f'{dt.now()}',
                    'message': 'PRE_EXAM'
                }
            )
            if variables.lp_active_time >= variables.rp_active_time:
                variables.active_p = 'LEFT_P'
            else:
                variables.active_p = 'RIGHT_P'
            if variables.lp_active_acc_time >= variables.rp_active_acc_time:
                variables.active_acc_p = 'LEFT_P'
            else:
                variables.active_acc_p = 'RIGHT_P'
            if variables.lp_key_pushes >= variables.rp_key_pushes:
                variables.active_kpush_p = 'LEFT_P'
            else:
                variables.active_kpush_p = 'RIGHT_P'
            player_log.info(
                {
                    'time': f'{dt.now()}',
                    'message': 'PRE_EXAM',
                    'score': variables.score,
                    'stage_time': f'{variables.stage_time}',
                    'active_p': variables.active_p,
                    'lp_act_t': f'{variables.lp_active_time}',
                    'rp_act_t': f'{variables.rp_active_time}',
                    'active_acc_p': variables.active_acc_p,
                    'lp_acc_t': f'{variables.lp_active_acc_time}',
                    'rp_acc_t': f'{variables.rp_active_acc_time}',
                    'active_kpush_p': variables.active_kpush_p,
                    'lp_kpush': variables.lp_key_pushes,
                    'rp_kpush': variables.rp_key_pushes,
                    'coop_time': f'{variables.cooperative_time}',
                    'conflict_time': f'{variables.conflict_time}',
                    'max_dwall_speed': variables.dwall_speed,
                    'end_difficulty': variables.dwall_difficulty
                }
            )
            player_pos_log.info(
                {
                    'time': f'{dt.now()}',
                    'message': 'PRE_EXAM'
                }
            )
        # START EXAM SESSION
        if events.type == START_EXAM:
            # RESET VARIABLES
            variables.lp_active_time = td()
            variables.rp_active_time = td()
            variables.lp_active_acc_time = td()
            variables.rp_active_acc_time = td()
            variables.lp_key_pushes = 0
            variables.rp_key_pushes = 0
            variables.cooperative_time = td()
            variables.conflict_time = td()
            # PREPARE EXAM
            variables.dwall_speed = settings.exam_dwall_speed
            variables.acc_dwall_speed = variables.dwall_speed * 2
            variables.dwall_amount = settings.exam_dwall_amount
            variables.dwall_difficulty = settings.exam_difficulty
            variables.score = 0
            variables.start_stage_time = dt.now()
            event_log.info(
                {
                    'time': f'{dt.now()}',
                    'message': 'START_EXAM'
                }
            )
            player_log.info(
                {
                    'time': f'{dt.now()}',
                    'message': 'START_EXAM'
                }
            )
            player_pos_log.info(
                {
                    'time': f'{dt.now()}',
                    'message': 'START_EXAM'
                }
            )
            variables.pl_pos_log = True
            pygame.time.set_timer(PLAYER_POS, settings.PLPOSLOG_TIMER)
        # STOP STAGE
        if events.type == STOP_STAGE:
            pygame.time.set_timer(PLAYER_POS, 0)
            variables.pl_pos_log = False
            variables.stage_time = dt.now() - variables.start_stage_time
            event_log.info(
                {
                    'time': f'{dt.now()}',
                    'message': 'STOP_STAGE',
                    'stage_time': f'{variables.stage_time}'
                }
            )
            player_log.info(
                {
                    'time': f'{dt.now()}',
                    'message': 'STOP_STAGE',
                    'stage_time': f'{variables.stage_time}'
                }
            )
            player_pos_log.info(
                {
                    'time': f'{dt.now()}',
                    'message': 'STOP_STAGE',
                    'stage_time': f'{variables.stage_time}'
                }
            )
        # RESULT
        if events.type == RESULT:
            event_log.info(
                {
                    'time': f'{dt.now()}',
                    'message': 'RESULT'
                }
            )
            if variables.lp_active_time >= variables.rp_active_time:
                variables.active_p = 'LEFT_P'
            else:
                variables.active_p = 'RIGHT_P'
            if variables.lp_active_acc_time >= variables.rp_active_acc_time:
                variables.active_acc_p = 'LEFT_P'
            else:
                variables.active_acc_p = 'RIGHT_P'
            if variables.lp_key_pushes >= variables.rp_key_pushes:
                variables.active_kpush_p = 'LEFT_P'
            else:
                variables.active_kpush_p = 'RIGHT_P'
            player_log.info(
                {
                    'time': f'{dt.now()}',
                    'message': 'RESULT',
                    'score': variables.score,
                    'stage_time': f'{variables.stage_time}',
                    'active_p': variables.active_p,
                    'lp_act_t': f'{variables.lp_active_time}',
                    'rp_act_t': f'{variables.rp_active_time}',
                    'active_acc_p': variables.active_acc_p,
                    'lp_acc_t': f'{variables.lp_active_acc_time}',
                    'rp_acc_t': f'{variables.rp_active_acc_time}',
                    'active_kpush_p': variables.active_kpush_p,
                    'lp_kpush': variables.lp_key_pushes,
                    'rp_kpush': variables.rp_key_pushes,
                    'coop_time': f'{variables.cooperative_time}',
                    'conflict_time': f'{variables.conflict_time}',
                    'max_dwall_speed': variables.dwall_speed,
                    'end_difficulty': variables.dwall_difficulty
                }
            )
        # RESULT
        if events.type == PLAYER_POS:
            variables.pl_pos_log = True
        # QUIT APP
        if events.type == pygame.QUIT:
            event_log.info(
                {
                    'time': f'{dt.now()}',
                    'message': 'SESSION_END',
                    'SESSION': f'{settings.SESSION_DIR}'
                }
            )
            pygame.quit()
            sys.exit()
        # DWALL CHANGE DIFFICULTY
        if events.type == DWALL_DIFF:
            if variables.SESSION_STAGE == 'START_TRAIN':
                if variables.accelerate:
                    variables.dwall_speed = ((variables.dwall_speed / 2) +
                                             settings.dw_sp_step)
                    variables.acc_dwall_speed = variables.dwall_speed * 2
                else:
                    variables.dwall_speed += settings.dw_sp_step
                    variables.acc_dwall_speed = variables.dwall_speed * 2
                variables.dwall_changed = True
            elif variables.SESSION_STAGE == 'START_EXAM':
                if variables.accelerate:
                    variables.dwall_speed = ((variables.dwall_speed / 2) +
                                             settings.ex_dw_sp_step)
                    variables.acc_dwall_speed = variables.dwall_speed * 2
                else:
                    variables.dwall_speed += settings.ex_dw_sp_step
                    variables.acc_dwall_speed = variables.dwall_speed * 2
                variables.dwall_changed = True
                if variables.dwall_amount == settings.ex_dw_am_dif:
                    variables.dwall_difficulty -= settings.ex_dw_dif_step

        if variables.SESSION_STAGE not in ('START_MENU',
                                           'STOP_STAGE',
                                           'PRE_EXAM',
                                           'RESULT'):
            player_events(events)
