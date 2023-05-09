import pygame

import settings
import variables


def ui_menu(screen, font: pygame.font.Font):
    back = pygame.Rect(25, 25, settings.WIDTH - 50, settings.HEIGHT - 50)
    pygame.draw.rect(screen, (200, 200, 200), back)
    top = 30
    left = 30
    screen.blit(
        font.render(settings.NAME, True, 'black'),
        (left, top))
    screen.blit(
        font.render('Управление:', True, 'black'),
        (left, top*3))
    # ЛИ
    screen.blit(
        font.render('Левый игрок (ЛИ):', True, 'black'),
        (left, top*5))
    screen.blit(
        font.render('A и D - движение влево и вправо', True, 'black'),
        (left*2, top*6))
    screen.blit(
        font.render('S - ускорение', True, 'black'),
        (left*2, top*7))
    # ПИ
    screen.blit(
        font.render('Правый игрок (ПИ):', True, 'black'),
        (left, top*8))
    screen.blit(
        font.render('Стрелки < и > - движение влево и вправо', True, 'black'),
        (left*2, top*9))
    screen.blit(
        font.render('V (стрелка вниз) - ускорение', True, 'black'),
        (left*2, top*10))
    #
    screen.blit(
        font.render('Первый этап: Тренировка.', True, 'black'),
        (left, top*12))
    screen.blit(
        font.render('Чтобы начать, одновременно удерживайте W', True, 'black'),
        (left, top*14))
    screen.blit(
        font.render('и стрелку вверх (^)', True, 'black'),
        (left, top*15))
    # player
    screen.blit(
        font.render('Управляете этим квадратом.', True, 'black'),
        (settings.WIDTH * 0.27, settings.HEIGHT - top*4))
    square = pygame.Rect(settings.WIDTH // 2 - 50 // 2,
                         settings.HEIGHT - 50 - 30, 50, 50)
    pygame.draw.rect(screen, settings.square_color, square)
    # dwall
    screen.blit(
        font.render('Проходите подобные препятствия.', True, 'black'),
        (settings.WIDTH * 0.27, settings.HEIGHT - 350))
    dwall_list = [0, 0, 2, 3, 4, 0, 6, 7, 8, 9, 0]
    new_dwall = [pygame.Rect(70 * j - 70,
                             settings.HEIGHT-300,
                             settings.dblock_w,
                             settings.dblock_h) for j in dwall_list]
    [pygame.draw.rect(screen, settings.dblock_color, dblock)
        for dblock in new_dwall]



def ui_game(screen, font, player):
    hud = pygame.Rect(0, 0, settings.WIDTH, 30)
    pygame.draw.rect(screen, (200, 200, 200), hud)
    three = settings.WIDTH // 3
    screen.blit(
        font.render(f'Осталось: {variables.dwall_amount}', True, 'black'),
        (three - three * .7, 5))
    screen.blit(
        font.render(f'Попытки: {player.health}', True, 'black'),
        (three * 2 - three * .7, 5))
    screen.blit(
        font.render(f'Очки: {player.score}', True, 'black'),
        (settings.WIDTH - three * .7, 5))


def ui_pre_exam(screen, font):
    back = pygame.Rect(25, 25, settings.WIDTH - 50, settings.HEIGHT - 50)
    pygame.draw.rect(screen, (200, 200, 200), back)
    top = 30
    left = 30
    screen.blit(
        font.render('Результаты тренировки:', True, 'black'),
        (left, top))
    screen.blit(
        font.render(f'Общее время тренировки - {variables.stage_time}',
                    True, 'black'),
        (left, top*3))
    if variables.active_p == 'LEFT_P':
        player = 'ЛИ'
    else:
        player = 'ПИ'
    screen.blit(
        font.render(f'Самый активный игрок (по времени) - {player}',
                    True, 'black'),
        (left, top*4))
    if variables.active_kpush_p == 'LEFT_P':
        player = 'ЛИ'
    else:
        player = 'ПИ'
    screen.blit(
        font.render(f'Самый активный игрок (по нажатиям) - {player}',
                    True, 'black'),
        (left, top*5))
    if variables.active_acc_p == 'LEFT_P':
        player = 'ЛИ'
    else:
        player = 'ПИ'
    screen.blit(
        font.render(f'Больше всего ускорений - {player}',
                    True, 'black'),
        (left, top*6))
    screen.blit(
        font.render(f'Общее время кооперации - {variables.cooperative_time}',
                    True, 'black'),
        (left, top*7))
    screen.blit(
        font.render(f'Общее время конфликта - {variables.conflict_time}',
                    True, 'black'),
        (left, top*8))
    screen.blit(
        font.render(f'Количество очков - {variables.score}',
                    True, 'black'),
        (left, top*9))
    screen.blit(
        font.render('Второй этап: Зачёт.', True, 'black'),
        (left, top*12))
    screen.blit(
        font.render('Чтобы начать, одновременно удерживайте W', True, 'black'),
        (left, top*14))
    screen.blit(
        font.render('и стрелку вверх (^)', True, 'black'),
        (left, top*15))


def ui_result(screen, font):
    back = pygame.Rect(25, 25, settings.WIDTH - 50, settings.HEIGHT - 50)
    pygame.draw.rect(screen, (200, 200, 200), back)
    top = 30
    left = 30
    screen.blit(
        font.render('Результаты зачёта:', True, 'black'),
        (left, top))
    screen.blit(
        font.render(f'Общее время тренировки - {variables.stage_time}',
                    True, 'black'),
        (left, top*3))
    if variables.active_p == 'LEFT_P':
        player = 'ЛИ'
    else:
        player = 'ПИ'
    screen.blit(
        font.render(f'Самый активный игрок (по времени) - {player}',
                    True, 'black'),
        (left, top*4))
    if variables.active_kpush_p == 'LEFT_P':
        player = 'ЛИ'
    else:
        player = 'ПИ'
    screen.blit(
        font.render(f'Самый активный игрок (по нажатиям) - {player}',
                    True, 'black'),
        (left, top*5))
    if variables.active_acc_p == 'LEFT_P':
        player = 'ЛИ'
    else:
        player = 'ПИ'
    screen.blit(
        font.render(f'Больше всего ускорений - {player}',
                    True, 'black'),
        (left, top*6))
    screen.blit(
        font.render(f'Общее время кооперации - {variables.cooperative_time}',
                    True, 'black'),
        (left, top*7))
    screen.blit(
        font.render(f'Общее время конфликта - {variables.conflict_time}',
                    True, 'black'),
        (left, top*8))
    screen.blit(
        font.render(f'Количество очков - {variables.score}',
                    True, 'black'),
        (left, top*9))
