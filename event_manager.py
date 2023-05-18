import sys
import pygame
from datetime import datetime as dt, timedelta as td

import settings
import variables
from logger import setup_logger
from player import player_log, player_pos_log
from dwall import dwall_log


log_file = 'events.json'
event_log = setup_logger('event_logger', log_file)


def get_template(template: str):
    time = f'{dt.now()}'

    temp_coop_end = {
        'time': time,
        'message': 'COOP_END',
        'cooperation_time': str(variables.cooperative_time.seconds)
    }
    temp_conf_end = {
        'time': time,
        'message': 'CONFLICT_END',
        'conflict_time': str(variables.conflict_time.seconds)
    }
    temp_acc_end = {
        'time': time,
        'message': 'ACC_END',
        'accelerate_time': str(variables.accelerate_time.seconds)
    }

    temp_dict = {
        'temp_coop_end': temp_coop_end,
        'temp_conf_end': temp_conf_end,
        'temp_acc_end': temp_acc_end
    }

    return temp_dict[template]


def log_info(logger, template: str):
    return logger.info(get_template(template))


def print_results(stage):
    if variables.active_p == 'LEFT_P':
        player_p = 'ЛИ'
    else:
        player_p = 'ПИ'
    if variables.active_kpush_p == 'LEFT_P':
        player_kp = 'ЛИ'
    else:
        player_kp = 'ПИ'
    if variables.active_acc_p == 'LEFT_P':
        player_ap = 'ЛИ'
    else:
        player_ap = 'ПИ'
    if stage == 'PRE_EXAM':
        stage_name = 'Результаты тренировки:'
        stage_name_2 = 'тренировки'
    elif stage == 'RESULT':
        stage_name = 'Результаты зачёта:'
        stage_name_2 = 'зачёта'
    results_dict = [
        '',
        '---------------------------------------',
        f'{stage_name}',
        f'Количество очков - {variables.score}',
        f'Общее время {stage_name_2} - {variables.stage_time}',
        f'Самый активный игрок (по времени) - {player_p}',
        f'Самый активный игрок (по нажатиям) - {player_kp}',
        f'Больше всего ускорений - {player_ap}',
        f'Общее время кооперации - {variables.cooperative_time}',
        f'Общее время конфликта - {variables.conflict_time}',
        f'Общее время ускорения - {variables.accelerate_time}'
    ]
    results_file = 'results.txt'
    dir = (f'{settings.BASE_DIR}/{settings.BASE_LOGS_DIR}/'
           f'{settings.SESSION_DIR}/{results_file}')
    with open(dir, 'a') as f:
        f.write('\n'.join(results_dict))


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
                    'time': f'{dt.now()}',
                    'message': 'LP_LEFT_DOWN'
                }
            )
            if variables.cooperation:
                if not variables.coop_started:
                    variables.coop_started = True
                    variables.start_cooperative_time = dt.now()
                    player_log.info(
                        {
                            'time': f'{dt.now()}',
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
                                'time': f'{dt.now()}',
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
                            'time': f'{dt.now()}',
                            'message': 'CONFLICT_START'
                        }
                    )
        if events.key == settings.RIGHT_1:
            variables.lp_key_pushes += 1
            variables.lp_right_time = dt.now()
            player_log.info(
                {
                    'time': f'{dt.now()}',
                    'message': 'LP_RIGHT_DOWN'
                }
            )
            if variables.cooperation:
                if not variables.coop_started:
                    variables.coop_started = True
                    variables.start_cooperative_time = dt.now()
                    player_log.info(
                        {
                            'time': f'{dt.now()}',
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
                                'time': f'{dt.now()}',
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
                            'time': f'{dt.now()}',
                            'message': 'CONFLICT_START'
                        }
                    )
        if events.key == settings.ACCELERATE_1:
            variables.lp_key_pushes += 1
            variables.lp_accelerate_time = dt.now()
            player_log.info(
                {
                    'time': f'{dt.now()}',
                    'message': 'LP_ACCELERATE_DOWN'
                }
            )
            if variables.accelerate:
                if not variables.accelerate_started:
                    variables.accelerate_started = True
                    variables.start_accelerate_time = dt.now()
                    player_log.info(
                        {
                            'time': f'{dt.now()}',
                            'message': 'ACC_START'
                        }
                    )
        # RP
        if events.key == settings.LEFT_2:
            variables.rp_key_pushes += 1
            variables.rp_left_time = dt.now()
            player_log.info(
                {
                    'time': f'{dt.now()}',
                    'message': 'RP_LEFT_DOWN'
                }
            )
            if variables.cooperation:
                if not variables.coop_started:
                    variables.coop_started = True
                    variables.start_cooperative_time = dt.now()
                    player_log.info(
                        {
                            'time': f'{dt.now()}',
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
                                'time': f'{dt.now()}',
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
                            'time': f'{dt.now()}',
                            'message': 'CONFLICT_START'
                        }
                    )
        if events.key == settings.RIGHT_2:
            variables.rp_key_pushes += 1
            variables.rp_right_time = dt.now()
            player_log.info(
                {
                    'time': f'{dt.now()}',
                    'message': 'RP_RIGHT_DOWN'
                }
            )
            if variables.cooperation:
                if not variables.coop_started:
                    variables.coop_started = True
                    variables.start_cooperative_time = dt.now()
                    player_log.info(
                        {
                            'time': f'{dt.now()}',
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
                                'time': f'{dt.now()}',
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
                            'time': f'{dt.now()}',
                            'message': 'CONFLICT_START'
                        }
                    )
        if events.key == settings.ACCELERATE_2:
            variables.rp_key_pushes += 1
            variables.rp_accelerate_time = dt.now()
            player_log.info(
                {
                    'time': f'{dt.now()}',
                    'message': 'RP_ACCELERATE_DOWN'
                }
            )
            if variables.accelerate:
                if not variables.accelerate_started:
                    variables.accelerate_started = True
                    variables.start_accelerate_time = dt.now()
                    player_log.info(
                        {
                            'time': f'{dt.now()}',
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
                    'time': f'{dt.now()}',
                    'message': 'LP_LEFT_UP',
                    'time_pushed': str(new_date)
                }
            )
            if variables.coop_started:
                if not variables.cooperation:
                    variables.coop_started = False
                    variables.cooperative_time += (
                        dt.now() - variables.start_cooperative_time)
                    log_info(player_log, 'temp_coop_end')
            if variables.conflict_started:
                if not variables.conflict:
                    variables.conflict_started = False
                    variables.conflict_time += (
                        dt.now() - variables.start_conflict_time)
                    log_info(player_log, 'temp_conf_end')
        if events.key == settings.RIGHT_1:
            new_date = dt.now() - variables.lp_right_time
            variables.lp_active_time += new_date
            player_log.info(
                {
                    'time': f'{dt.now()}',
                    'message': 'LP_RIGHT_UP',
                    'time_pushed': str(new_date)
                }
            )
            if variables.coop_started:
                if not variables.cooperation:
                    variables.coop_started = False
                    variables.cooperative_time += (
                        dt.now() - variables.start_cooperative_time)
                    log_info(player_log, 'temp_coop_end')
            if variables.conflict_started:
                if not variables.conflict:
                    variables.conflict_started = False
                    variables.conflict_time += (
                        dt.now() - variables.start_conflict_time)
                    log_info(player_log, 'temp_conf_end')
        if events.key == settings.ACCELERATE_1:
            new_date = dt.now() - variables.lp_accelerate_time
            variables.lp_active_acc_time += new_date
            player_log.info(
                {
                    'time': f'{dt.now()}',
                    'message': 'LP_ACCELERATE_UP',
                    'time_pushed': str(new_date)
                }
            )
            if variables.accelerate_started:
                if not variables.accelerate:
                    variables.accelerate_started = False
                    variables.accelerate_time += (
                        dt.now() - variables.start_accelerate_time)
                    log_info(player_log, 'temp_acc_end')
        # RP
        if events.key == settings.LEFT_2:
            new_date = dt.now() - variables.rp_left_time
            variables.rp_active_time += new_date
            player_log.info(
                {
                    'time': f'{dt.now()}',
                    'message': 'RP_LEFT_UP',
                    'time_pushed': str(new_date)
                }
            )
            if variables.coop_started:
                if not variables.cooperation:
                    variables.coop_started = False
                    variables.cooperative_time += (
                        dt.now() - variables.start_cooperative_time)
                    log_info(player_log, 'temp_coop_end')
            if variables.conflict_started:
                if not variables.conflict:
                    variables.conflict_started = False
                    variables.conflict_time += (
                        dt.now() - variables.start_conflict_time)
                    log_info(player_log, 'temp_conf_end')
        if events.key == settings.RIGHT_2:
            new_date = dt.now() - variables.rp_right_time
            variables.rp_active_time += new_date
            player_log.info(
                {
                    'time': f'{dt.now()}',
                    'message': 'RP_RIGHT_UP',
                    'time_pushed': str(new_date)
                }
            )
            if variables.coop_started:
                if not variables.cooperation:
                    variables.coop_started = False
                    variables.cooperative_time += (
                        dt.now() - variables.start_cooperative_time)
                    log_info(player_log, 'temp_coop_end')
            if variables.conflict_started:
                if not variables.conflict:
                    variables.conflict_started = False
                    variables.conflict_time += (
                        dt.now() - variables.start_conflict_time)
                    log_info(player_log, 'temp_conf_end')
        if events.key == settings.ACCELERATE_2:
            new_date = dt.now() - variables.rp_accelerate_time
            variables.rp_active_acc_time += new_date
            player_log.info(
                {
                    'time': f'{dt.now()}',
                    'message': 'RP_ACCELERATE_UP',
                    'time_pushed': str(new_date)
                }
            )
            if variables.accelerate_started:
                if not variables.accelerate:
                    variables.accelerate_started = False
                    variables.accelerate_time += (
                        dt.now() - variables.start_accelerate_time)
                    log_info(player_log, 'temp_acc_end')


def event_handler():
    for events in pygame.event.get():
        # EVENTS SECTION
        # PLAYER POS LOGS
        if events.type == settings.PLAYER_POS:
            variables.pl_pos_log = True
        # DWALL CHANGE DIFFICULTY
        if events.type == settings.DWALL_DIFF:
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
                if variables.dwall_amount in (settings.ex_dw_am_dif_1,
                                              settings.ex_dw_am_dif_2):
                    variables.dwall_difficulty -= settings.ex_dw_dif_step
        # RESULT
        if events.type == settings.RESULT:
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
            if variables.accelerate:
                variables.dwall_speed *= .5
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
                    'end_difficulty': variables.dwall_difficulty,
                    'dwall_amount': variables.dwall_amount
                }
            )
            print_results('RESULT')
        # STOP STAGE
        elif events.type == settings.STOP_STAGE:
            # stop pl pos logs
            pygame.time.set_timer(settings.PLAYER_POS, 0)
            variables.pl_pos_log = False
            # check coop, conflict and acc stopping
            if variables.coop_started:
                variables.coop_started = False
                variables.cooperative_time += (
                    dt.now() - variables.start_cooperative_time)
                log_info(player_log, 'temp_coop_end')
            if variables.conflict_started:
                variables.conflict_started = False
                variables.conflict_time += (
                    dt.now() - variables.start_conflict_time)
                log_info(player_log, 'temp_conf_end')
            if variables.accelerate_started:
                variables.accelerate_started = False
                variables.accelerate_time += (
                    dt.now() - variables.start_accelerate_time)
                log_info(player_log, 'temp_acc_end')
            # logs
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
            dwall_log.info(
                {
                    'time': f'{dt.now()}',
                    'message': 'STOP_STAGE',
                    'stage_time': f'{variables.stage_time}'
                }
            )
        # START EXAM SESSION
        elif events.type == settings.START_EXAM:
            # RESET VARIABLES
            variables.is_warmuped = False
            variables.lp_active_time = td()
            variables.rp_active_time = td()
            variables.lp_active_acc_time = td()
            variables.rp_active_acc_time = td()
            variables.lp_key_pushes = 0
            variables.rp_key_pushes = 0
            variables.cooperative_time = td()
            variables.conflict_time = td()
            variables.accelerate_time = td()
            # PREPARE EXAM
            variables.dwall_speed = settings.exam_dwall_speed
            variables.acc_dwall_speed = variables.dwall_speed * 2
            variables.dwall_amount = settings.exam_dwall_amount
            variables.dwall_difficulty = settings.exam_difficulty
            variables.score = 0
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
            dwall_log.info(
                {
                    'time': f'{dt.now()}',
                    'message': 'START_EXAM'
                }
            )
        # PRE EXAM STATE
        elif events.type == settings.PRE_EXAM:
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
            if variables.accelerate:
                variables.dwall_speed *= .5
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
                    'end_difficulty': variables.dwall_difficulty,
                    'dwall_amount': variables.dwall_amount
                }
            )
            print_results('PRE_EXAM')
            player_pos_log.info(
                {
                    'time': f'{dt.now()}',
                    'message': 'PRE_EXAM'
                }
            )
            event_log.info(
                {
                    'time': f'{dt.now()}',
                    'message': 'PRE_EXAM'
                }
            )
            dwall_log.info(
                {
                    'time': f'{dt.now()}',
                    'message': 'PRE_EXAM'
                }
            )
        # START TRAIN STATE
        elif events.type == settings.START_TRAIN:
            variables.is_warmuped = False
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
            dwall_log.info(
                {
                    'time': f'{dt.now()}',
                    'message': 'START_TRAIN'
                }
            )
        # START MENU
        elif events.type == settings.START_MENU:
            event_log.info(
                {
                    'time': f'{dt.now()}',
                    'message': 'START_MENU',
                    'SESSION': f'{settings.SESSION_DIR}'
                }
            )
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
        # ACTIVATE DEBUG PANEL AND EXIT
        if events.type == pygame.KEYDOWN:
            if events.mod == pygame.KMOD_LALT:
                if events.key == settings.DEBUG:
                    if not variables.debug_activated:
                        variables.debug_activated = True
                    else:
                        variables.debug_activated = False
                if events.key == settings.EXIT:
                    pygame.event.post(pygame.event.Event(pygame.QUIT))

        if variables.SESSION_STAGE in ('START_TRAIN', 'START_EXAM'):
            player_events(events)
