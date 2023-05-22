import pygame
from datetime import datetime as dt

import settings
from settings import dark_grey, accent
import variables
from fonts import (title1, title2, base, base2)


def ui_credits(screen):
    top = 30
    left = 70
    center = settings.WIDTH // 2
    #
    t = title1.render(settings.NAME, True, dark_grey)
    screen.blit(t,
                (center - t.get_width()*.5, top))
    screen.blit(base2.render('Идея', True, dark_grey),
                (left, top*4))
    text = base2.render('Машков Н.А.', True, dark_grey)
    screen.blit(text,
                (settings.WIDTH - left - text.get_width(), top*4))
    screen.blit(base2.render('Разработка', True, dark_grey),
                (left, top*5.5))
    text = base2.render('Машков Н.А.', True, dark_grey)
    screen.blit(text,
                (settings.WIDTH - left - text.get_width(), top*5.5))
    screen.blit(base2.render('Дизайн', True, dark_grey),
                (left, top*7))
    text = base2.render('Мануйленко Е.В.', True, dark_grey)
    screen.blit(text,
                (settings.WIDTH - left - text.get_width(), top*7))
    #
    text = base2.render('СПбГУ ГА', True, dark_grey)
    screen.blit(text,
                (settings.WIDTH // 2 - text.get_width()*.5, top*11))
    text = base.render('2023', True, dark_grey)
    screen.blit(text,
                (settings.WIDTH // 2 - text.get_width()*.5, top*12))
    # dwall
    dwall_list = [0, 0, 2, 3, 4, 0, 0, 7, 8, 9, 0]
    new_dwall = [pygame.Rect(70 * j - 70,
                             settings.HEIGHT-250,
                             settings.dblock_w,
                             settings.dblock_h) for j in dwall_list]
    [pygame.draw.rect(screen, settings.dblock_color, dblock)
        for dblock in new_dwall]
    # player
    square = pygame.Rect(settings.WIDTH // 2 - 50 // 2,
                         settings.HEIGHT - 50 - 30, 50, 50)
    pygame.draw.rect(screen, settings.square_color, square)


def ui_menu(screen: pygame.Surface):
    top = 30
    left = 70
    center = settings.WIDTH // 2
    #
    t = title1.render(settings.NAME, True, dark_grey)
    screen.blit(t,
                (center - t.get_width()*.5, top))
    screen.blit(title2.render('Управление', True, dark_grey),
                (center - 70, top*3.5))
    # ЛИ
    screen.blit(base2.render('Левый игрок (ЛИ)', True, dark_grey),  # 175
                (left, top*5.5))
    button = pygame.Rect(left + 175*.2 - 20, top*7.5-8, 40, 40)
    pygame.draw.rect(screen, accent, button, width=2, border_radius=10)
    button = pygame.Rect(left + 175*.8 - 20, top*7.5-8, 40, 40)
    pygame.draw.rect(screen, accent, button, width=2, border_radius=10)
    screen.blit(base2.render('A', True, dark_grey),  # 14
                (left + 175*.2 - 7, top*7.5))
    screen.blit(base2.render('D', True, dark_grey),  # 14
                (left + 175*.8 - 7, top*7.5))
    screen.blit(base.render('Движение влево и вправо', True, dark_grey),
                (left + (175 - 205)*.5, top*9))
    button = pygame.Rect(left + 175*.5 - 20, top*10.5-8, 40, 40)
    pygame.draw.rect(screen, accent, button, width=2, border_radius=10)
    screen.blit(base2.render('S', True, dark_grey),  # 13
                (left + 175*.5 - 13*.5, top*10.5))
    screen.blit(base.render('Ускорение', True, dark_grey),  # 83
                (left + (175 - 83)*.5, top*12))
    # ПИ
    screen.blit(base2.render('Правый игрок (ПИ)', True, dark_grey),  # 188
                (settings.WIDTH - left - 188, top*5.5))
    button = pygame.Rect(settings.WIDTH-left-188*.8-37, top*7.5-8, 74, 40)
    pygame.draw.rect(screen, accent, button, width=2, border_radius=10)
    button = pygame.Rect(settings.WIDTH-left-188*.2-43, top*7.5-8, 86, 40)
    pygame.draw.rect(screen, accent, button, width=2, border_radius=10)
    screen.blit(base2.render('LEFT', True, dark_grey),  # 48
                (settings.WIDTH - left - 188*.8 - 24, top*7.5))
    screen.blit(base2.render('RIGHT', True, dark_grey),  # 61
                (settings.WIDTH - left - 188*.2 - 30, top*7.5))
    screen.blit(base.render('Движение влево и вправо', True, dark_grey),  # 205
                (settings.WIDTH - left - (205 + 188)*.5, top*9))
    button = pygame.Rect(settings.WIDTH-left-(188+89)*.5, top*10.5-8, 89, 40)
    pygame.draw.rect(screen, accent, button, width=2, border_radius=10)
    screen.blit(base2.render('DOWN', True, dark_grey),  # 63
                (settings.WIDTH-left-(188+63)*.5, top*10.5))
    screen.blit(base.render('Ускорение', True, dark_grey),  # 83
                (settings.WIDTH-left-(188+83)*.5, top*12))
    #
    screen.blit(base2.render('Первый этап', True, dark_grey),  # 125
                (left + (175 - 125)*.5, top*14))
    screen.blit(base.render('Тренировка', True, dark_grey),  # 94
                (left + (175 - 94)*.5, top*15))
    #
    screen.blit(base2.render('Препятствий', True, dark_grey),  # 128
                (settings.WIDTH - left - (128 + 188)*.5, top*14))
    screen.blit(base.render('30', True, dark_grey),  # 20
                (settings.WIDTH - left - (20 + 188)*.5, top*15))
    #
    button = pygame.Rect(center-263, top*18-10, 526, 40)
    pygame.draw.rect(screen, accent, button, width=2, border_radius=10)
    screen.blit(base.render('Чтобы начать, одновременно нажмите W и '
                            'стрелку вверх (UP)', True, dark_grey),
                (center - 251, top*18))
    # dwall
    screen.blit(
        base.render('Проходите подобные препятствия', True, dark_grey),
        (center - 274*.5, settings.HEIGHT - 280))  # 274
    dwall_list = [0, 0, 2, 3, 4, 0, 0, 7, 8, 9, 0]
    new_dwall = [pygame.Rect(70 * j - 70,
                             settings.HEIGHT-250,
                             settings.dblock_w,
                             settings.dblock_h) for j in dwall_list]
    [pygame.draw.rect(screen, settings.dblock_color, dblock)
        for dblock in new_dwall]
    # player
    screen.blit(base.render('Управляйте этим квадратом', True, dark_grey),
                (center - 226*.5, settings.HEIGHT - top*3.5))  # 226
    square = pygame.Rect(settings.WIDTH // 2 - 50 // 2,
                         settings.HEIGHT - 50 - 30, 50, 50)
    pygame.draw.rect(screen, settings.square_color, square)
    #
    date = dt.now()
    if len(str(date.minute)) > 1:
        minutes = date.minute
    else:
        minutes = f'0{date.minute}'
    text = base.render(f'{date.hour}:{minutes}-'
                       f'{str(settings.SESSION_DIR)[:8]}',
                       True, dark_grey)
    screen.blit(text, (center - text.get_width()*.5,
                       settings.HEIGHT - text.get_height()))


def ui_game(screen, player):
    hud = pygame.Rect(0, 0, settings.WIDTH, 30)
    pygame.draw.rect(screen, (255, 255, 255), hud,
                     border_bottom_left_radius=10,
                     border_bottom_right_radius=10)
    three = settings.WIDTH // 3
    screen.blit(
        base2.render(f'Осталось: {variables.dwall_amount}', True, dark_grey),
        (three * .5 - 65, 5))  # 130
    screen.blit(base2.render(f'Попытки: {player.health}', True, dark_grey),
                (settings.WIDTH // 2 - 56, 5))
    screen.blit(base2.render(f'Очки: {player.score}', True, dark_grey),
                (settings.WIDTH - three * .5 - 37, 5))


def ui_pre_exam(screen):
    top = 30
    left = 30
    center = settings.WIDTH // 2
    #
    screen.blit(title1.render('Результаты тренировки', True, dark_grey),  # 481
                (center - 481*.5, top))
    #
    screen.blit(base2.render('Общее время тренировки', True, dark_grey),  # 256
                (left, top*4))
    text = base2.render(f'{variables.stage_time}', True, dark_grey)
    screen.blit(text,
                (settings.WIDTH - left - text.get_width(), top*4))
    if variables.active_p == 'LEFT_P':
        player = 'ЛИ'
    else:
        player = 'ПИ'
    screen.blit(base2.render('Самый активный игрок (по времени)',
                             True, dark_grey),
                (left, top*5))
    screen.blit(base2.render(f'{player}', True, dark_grey),  # 29
                (settings.WIDTH - left - 29, top*5))
    if variables.active_kpush_p == 'LEFT_P':
        player = 'ЛИ'
    else:
        player = 'ПИ'
    screen.blit(base2.render('Самый активный игрок (по нажатиям)',
                             True, dark_grey),
                (left, top*6))
    screen.blit(base2.render(f'{player}', True, dark_grey),
                (settings.WIDTH - left - 29, top*6))
    if variables.active_acc_p == 'LEFT_P':
        player = 'ЛИ'
    else:
        player = 'ПИ'
    screen.blit(base2.render('Больше всего ускорений', True, dark_grey),
                (left, top*7))
    screen.blit(base2.render(f'{player}', True, dark_grey),
                (settings.WIDTH - left - 29, top*7))
    screen.blit(base2.render('Общее время кооперации', True, dark_grey),
                (left, top*8))
    text = base2.render(f'{variables.cooperative_time}', True, dark_grey)
    screen.blit(text,
                (settings.WIDTH - left - text.get_width(), top*8))
    screen.blit(base2.render('Общее время конфликта', True, dark_grey),
                (left, top*9))
    text = base2.render(f'{variables.conflict_time}', True, dark_grey)
    screen.blit(text,
                (settings.WIDTH - left - text.get_width(), top*9))
    screen.blit(base2.render('Общее время ускорения', True, dark_grey),
                (left, top*10))
    text = base2.render(f'{variables.accelerate_time}', True, dark_grey)
    screen.blit(text,
                (settings.WIDTH - left - text.get_width(), top*10))
    screen.blit(base2.render('Количество очков', True, dark_grey),
                (left, top*11))
    t = base2.render(f'{variables.score}', True, dark_grey)
    screen.blit(t, (settings.WIDTH - left - t.get_width(), top*11))
    #
    left = 70
    screen.blit(base2.render('Второй этап', True, dark_grey),  # 120
                (left + (175 - 120)*.5, top*14))
    screen.blit(base.render('Зачёт', True, dark_grey),  # 45
                (left + (175 - 45)*.5, top*15))
    #
    screen.blit(base2.render('Препятствий', True, dark_grey),  # 128
                (settings.WIDTH - left - (128 + 188)*.5, top*14))
    t = base.render(f'{settings.exam_dwall_amount}', True, dark_grey)
    screen.blit(t, (settings.WIDTH - left - (t.get_width() + 188)*.5, top*15))
    #
    button = pygame.Rect(center-263, top*18-10, 526, 40)
    pygame.draw.rect(screen, accent, button, width=2, border_radius=10)
    screen.blit(base.render('Чтобы начать, одновременно нажмите W и '
                            'стрелку вверх (UP)', True, dark_grey),
                (center - 251, top*18))
    #
    date = dt.now()
    if len(str(date.minute)) > 1:
        minutes = date.minute
    else:
        minutes = f'0{date.minute}'
    text = base.render(f'{date.hour}:{minutes}-'
                       f'{str(settings.SESSION_DIR)[:8]}',
                       True, dark_grey)
    screen.blit(text, (center - text.get_width()*.5,
                       settings.HEIGHT - text.get_height()))


def ui_result(screen):
    top = 30
    left = 30
    center = settings.WIDTH // 2
    #
    screen.blit(title1.render('Результаты зачёта', True, dark_grey),  # 377
                (center - 377*.5, top))
    #
    screen.blit(base2.render('Общее время зачёта', True, dark_grey),
                (left, top*4))
    text = base2.render(f'{variables.stage_time}', True, dark_grey)
    screen.blit(text,
                (settings.WIDTH - left - text.get_width(), top*4))
    if variables.active_p == 'LEFT_P':
        player = 'ЛИ'
    else:
        player = 'ПИ'
    screen.blit(base2.render('Самый активный игрок (по времени)',
                             True, dark_grey),
                (left, top*5))
    screen.blit(base2.render(f'{player}', True, dark_grey),  # 29
                (settings.WIDTH - left - 29, top*5))
    if variables.active_kpush_p == 'LEFT_P':
        player = 'ЛИ'
    else:
        player = 'ПИ'
    screen.blit(base2.render('Самый активный игрок (по нажатиям)',
                             True, dark_grey),
                (left, top*6))
    screen.blit(base2.render(f'{player}', True, dark_grey),
                (settings.WIDTH - left - 29, top*6))
    if variables.active_acc_p == 'LEFT_P':
        player = 'ЛИ'
    else:
        player = 'ПИ'
    screen.blit(base2.render('Больше всего ускорений', True, dark_grey),
                (left, top*7))
    screen.blit(base2.render(f'{player}', True, dark_grey),
                (settings.WIDTH - left - 29, top*7))
    screen.blit(base2.render('Общее время кооперации', True, dark_grey),
                (left, top*8))
    text = base2.render(f'{variables.cooperative_time}', True, dark_grey)
    screen.blit(text,
                (settings.WIDTH - left - text.get_width(), top*8))
    screen.blit(base2.render('Общее время конфликта', True, dark_grey),
                (left, top*9))
    text = base2.render(f'{variables.conflict_time}', True, dark_grey)
    screen.blit(text,
                (settings.WIDTH - left - text.get_width(), top*9))
    screen.blit(base2.render('Общее время ускорения', True, dark_grey),
                (left, top*10))
    text = base2.render(f'{variables.accelerate_time}', True, dark_grey)
    screen.blit(text,
                (settings.WIDTH - left - text.get_width(), top*10))
    screen.blit(base2.render('Количество очков', True, dark_grey),
                (left, top*11))
    t = base2.render(f'{variables.score}', True, dark_grey)
    screen.blit(t, (settings.WIDTH - left - t.get_width(), top*11))
    #
    button = pygame.Rect(center-151, top*18-10, 302, 40)
    pygame.draw.rect(screen, accent, button, width=2, border_radius=10)
    screen.blit(base.render('Чтобы завершить, нажмите ENTER', True, dark_grey),
                (center - 276*.5, top*18))  # 276
    #
    date = dt.now()
    if len(str(date.minute)) > 1:
        minutes = date.minute
    else:
        minutes = f'0{date.minute}'
    text = base.render(f'{date.hour}:{minutes}-'
                       f'{str(settings.SESSION_DIR)[:8]}',
                       True, dark_grey)
    screen.blit(text, (center - text.get_width()*.5,
                       settings.HEIGHT - text.get_height()))
    # t = base2.render('DOWN', True, dark_grey)
    # print(t.get_width())
