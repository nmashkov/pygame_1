import pygame

import settings
from settings import dark_grey
import variables
from fonts import (title1, title2, base2)


def ui_menu(screen):
    top = 30
    left = 30
    screen.blit(
        title1.render(settings.NAME, True, dark_grey),
        (left, top))
    screen.blit(
        title2.render('Управление:', True, dark_grey),
        (left, top*3))
    # ЛИ
    screen.blit(
        title2.render('Левый игрок (ЛИ):', True, dark_grey),
        (left, top*5))
    screen.blit(
        base2.render('A и D - движение влево и вправо', True, dark_grey),
        (left*2, top*6))
    screen.blit(
        base2.render('S - ускорение', True, dark_grey),
        (left*2, top*7))
    # ПИ
    screen.blit(
        title2.render('Правый игрок (ПИ):', True, dark_grey),
        (left, top*8))
    screen.blit(
        base2.render('LEFT и RIGHT - движение влево и вправо',
                     True, dark_grey),
        (left*2, top*9))
    screen.blit(
        base2.render('DOWN - ускорение', True, dark_grey),
        (left*2, top*10))
    #
    screen.blit(
        title2.render('Первый этап: Тренировка.', True, dark_grey),
        (left, top*12))
    screen.blit(
        base2.render('Чтобы начать, одновременно удерживайте W',
                     True, dark_grey),
        (left, top*14))
    screen.blit(
        base2.render('и стрелку вверх (UP)', True, dark_grey),
        (left, top*15))
    # dwall
    screen.blit(
        title2.render('Проходите подобные препятствия.', True, dark_grey),
        (settings.WIDTH * 0.2, settings.HEIGHT - 350))
    dwall_list = [0, 0, 2, 3, 4, 0, 6, 7, 8, 9, 0]
    new_dwall = [pygame.Rect(70 * j - 70,
                             settings.HEIGHT-300,
                             settings.dblock_w,
                             settings.dblock_h) for j in dwall_list]
    [pygame.draw.rect(screen, settings.dblock_color, dblock)
        for dblock in new_dwall]
    # player
    screen.blit(
        title2.render('Управляйте этим квадратом.', True, dark_grey),
        (settings.WIDTH * 0.27, settings.HEIGHT - top*4))
    square = pygame.Rect(settings.WIDTH // 2 - 50 // 2,
                         settings.HEIGHT - 50 - 30, 50, 50)
    pygame.draw.rect(screen, settings.square_color, square)


def ui_game(screen, player):
    hud = pygame.Rect(0, 0, settings.WIDTH, 30)
    pygame.draw.rect(screen, (255, 255, 255), hud)
    three = settings.WIDTH // 3
    screen.blit(
        base2.render(f'Осталось: {variables.dwall_amount}', True, dark_grey),
        (three - three * .7, 5))
    screen.blit(
        base2.render(f'Попытки: {player.health}', True, dark_grey),
        (three * 2 - three * .7, 5))
    screen.blit(
        base2.render(f'Очки: {player.score}', True, dark_grey),
        (settings.WIDTH - three * .7, 5))


def ui_pre_exam(screen):
    top = 30
    left = 30
    screen.blit(
        title2.render('Результаты тренировки:', True, dark_grey),
        (left, top))
    screen.blit(
        base2.render(f'Общее время тренировки - {variables.stage_time}',
                     True, dark_grey),
        (left, top*3))
    if variables.active_p == 'LEFT_P':
        player = 'ЛИ'
    else:
        player = 'ПИ'
    screen.blit(
        base2.render(f'Самый активный игрок (по времени) - {player}',
                     True, dark_grey),
        (left, top*4))
    if variables.active_kpush_p == 'LEFT_P':
        player = 'ЛИ'
    else:
        player = 'ПИ'
    screen.blit(
        base2.render(f'Самый активный игрок (по нажатиям) - {player}',
                     True, dark_grey),
        (left, top*5))
    if variables.active_acc_p == 'LEFT_P':
        player = 'ЛИ'
    else:
        player = 'ПИ'
    screen.blit(
        base2.render(f'Больше всего ускорений - {player}',
                     True, dark_grey),
        (left, top*6))
    screen.blit(
        base2.render(f'Общее время кооперации - {variables.cooperative_time}',
                     True, dark_grey),
        (left, top*7))
    screen.blit(
        base2.render(f'Общее время конфликта - {variables.conflict_time}',
                     True, dark_grey),
        (left, top*8))
    screen.blit(
        base2.render(f'Общее время ускорения - {variables.accelerate_time}',
                     True, dark_grey),
        (left, top*9))
    screen.blit(
        base2.render(f'Количество очков - {variables.score}',
                     True, dark_grey),
        (left, top*10))
    screen.blit(
        title2.render('Второй этап: Зачёт.', True, dark_grey),
        (left, top*13))
    screen.blit(
        base2.render('Чтобы начать, одновременно удерживайте W',
                     True, dark_grey),
        (left, top*15))
    screen.blit(
        base2.render('и стрелку вверх (UP)', True, dark_grey),
        (left, top*16))


def ui_result(screen):
    top = 30
    left = 30
    screen.blit(
        title2.render('Результаты зачёта:', True, dark_grey),
        (left, top))
    screen.blit(
        base2.render(f'Общее время тренировки - {variables.stage_time}',
                     True, dark_grey),
        (left, top*3))
    if variables.active_p == 'LEFT_P':
        player = 'ЛИ'
    else:
        player = 'ПИ'
    screen.blit(
        base2.render(f'Самый активный игрок (по времени) - {player}',
                     True, dark_grey),
        (left, top*4))
    if variables.active_kpush_p == 'LEFT_P':
        player = 'ЛИ'
    else:
        player = 'ПИ'
    screen.blit(
        base2.render(f'Самый активный игрок (по нажатиям) - {player}',
                     True, dark_grey),
        (left, top*5))
    if variables.active_acc_p == 'LEFT_P':
        player = 'ЛИ'
    else:
        player = 'ПИ'
    screen.blit(
        base2.render(f'Больше всего ускорений - {player}',
                     True, dark_grey),
        (left, top*6))
    screen.blit(
        base2.render(f'Общее время кооперации - {variables.cooperative_time}',
                     True, dark_grey),
        (left, top*7))
    screen.blit(
        base2.render(f'Общее время конфликта - {variables.conflict_time}',
                     True, dark_grey),
        (left, top*8))
    screen.blit(
        base2.render(f'Общее время ускорения - {variables.accelerate_time}',
                     True, dark_grey),
        (left, top*9))
    screen.blit(
        base2.render(f'Количество очков - {variables.score}',
                     True, dark_grey),
        (left, top*10))
