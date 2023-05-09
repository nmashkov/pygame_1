import pygame

import settings
import variables
from debug import debug


def ui_menu(screen, font: pygame.font.Font):
    screen.blit(
        font.render(variables.SESSION_STAGE, True, 'black'),
        (settings.WIDTH // 2, 10))


def ui_game(screen, font):
    screen.blit(
        font.render(variables.SESSION_STAGE, True, 'black'),
        (settings.WIDTH // 2, 10))


def ui_pre_exam(screen, font):
    screen.blit(
        font.render(variables.SESSION_STAGE, True, 'black'),
        (settings.WIDTH // 2, 10))

    debug(variables.stage_time)
    debug(variables.active_p, 30)
    debug(variables.lp_active_time, 50)
    debug(variables.rp_active_time, 70)
    debug(variables.active_acc_p, 90)
    debug(variables.lp_active_acc_time, 110)
    debug(variables.rp_active_acc_time, 130)
    debug(variables.active_kpush_p, 150)
    debug(variables.lp_key_pushes, 170)
    debug(variables.rp_key_pushes, 190)
    debug(variables.cooperative_time, 210)
    debug(variables.conflict_time, 230)
    debug(variables.score, 250)
    debug(variables.dwall_speed, 270)
    debug(variables.dwall_difficulty, 290)


def ui_result(screen, font):
    screen.blit(
        font.render(variables.SESSION_STAGE, True, 'black'),
        (settings.WIDTH // 2, 10))

    debug(variables.stage_time)
    debug(variables.active_p, 30)
    debug(variables.lp_active_time, 50)
    debug(variables.rp_active_time, 70)
    debug(variables.active_acc_p, 90)
    debug(variables.lp_active_acc_time, 110)
    debug(variables.rp_active_acc_time, 130)
    debug(variables.active_kpush_p, 150)
    debug(variables.lp_key_pushes, 170)
    debug(variables.rp_key_pushes, 190)
    debug(variables.cooperative_time, 210)
    debug(variables.conflict_time, 230)
    debug(variables.score, 250)
    debug(variables.dwall_speed, 270)
    debug(variables.dwall_difficulty, 290)
