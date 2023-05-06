import pygame
from datetime import datetime as dt

from logger import setup_logger
from player import player_log
import settings
import variables


log_file = './logs/events.json'
event_log = setup_logger('event_logger', log_file)


START_MENU = pygame.USEREVENT + 1
START_TRAIN = pygame.USEREVENT + 2
START_EXAM = pygame.USEREVENT + 3
STOP_STAGE = pygame.USEREVENT + 4


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
    # [exit() for i in pygame.event.get() if i.type == pygame.QUIT]

    for events in pygame.event.get():
        # EVENTS SECTION
        # START MENU
        if events.type == START_MENU:
            event_log.info(
                {
                    'time': str(dt.now()),
                    'message': 'START_MENU'
                }
            )
        # START TRAIN SESSION
        if events.type == START_TRAIN:
            event_log.info(
                {
                    'time': str(dt.now()),
                    'message': 'START_TRAIN'
                }
            )
            player_log.info(
                {
                    'time': str(dt.now()),
                    'message': 'START_TRAIN'
                }
            )
        # START EXAM SESSION
        if events.type == START_EXAM:
            event_log.info(
                {
                    'time': str(dt.now()),
                    'message': 'START_EXAM'
                }
            )
            player_log.info(
                {
                    'time': str(dt.now()),
                    'message': 'START_EXAM'
                }
            )
        # STOP STAGE
        if events.type == STOP_STAGE:
            variables.stage_time = dt.now() - variables.start_stage_time
            event_log.info(
                {
                    'time': str(dt.now()),
                    'message': 'STOP_STAGE',
                    'stage_time': f'{variables.stage_time}'
                }
            )
            active_p = 'LEFT_P'
            if variables.lp_active_time >= variables.rp_active_time:
                active_p = 'LEFT_P'
            else:
                active_p = 'RIGHT_P'
            active_acc_p = ''
            if variables.lp_active_acc_time >= variables.rp_active_acc_time:
                active_acc_p = 'LEFT_P'
            else:
                active_acc_p = 'RIGHT_P'
            active_kpush_p = ''
            if variables.lp_key_pushes >= variables.rp_key_pushes:
                active_kpush_p = 'LEFT_P'
            else:
                active_kpush_p = 'RIGHT_P'
            player_log.info(
                {
                    'time': str(dt.now()),
                    'message': 'STOP_STAGE',
                    'stage_time': f'{variables.stage_time}',
                    'active_p': active_p,
                    'lp_act_t': f'{variables.lp_active_time}',
                    'rp_act_t': f'{variables.rp_active_time}',
                    'active_acc_p': active_acc_p,
                    'lp_acc_t': f'{variables.lp_active_acc_time}',
                    'rp_acc_t': f'{variables.rp_active_acc_time}',
                    'active_kpush_p': active_kpush_p,
                    'lp_kpush': variables.lp_key_pushes,
                    'rp_kpush': variables.rp_key_pushes,
                    'coop_time': f'{variables.cooperative_time}',
                    'conflict_time': f'{variables.conflict_time}'
                }
            )
        # QUIT APP
        if events.type == pygame.QUIT:
            # pygame.quit()
            # quit()
            event_log.info(
                {
                    'time': str(dt.now()),
                    'message': 'SESSION_END'
                }
            )
            exit()

        if variables.SESSION_STAGE not in ('START_MENU', 'STOP_STAGE'):
            player_events(events)
