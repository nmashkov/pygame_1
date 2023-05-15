"""
Game 1.
Author: Nikita Mashkov
Programmer: Nikita Mashkov
Design: Evgeny Manuylenko
Github: https://github.com/nmashkov
2023
"""
import pygame
from datetime import datetime as dt

import settings
import variables
from player import Player
from dwall import Dwall
from event_manager import event_handler
from fonts import base2
import ui
# from debug import debug
# debug(info, pygame.mouse.get_pos()[1], pygame.mouse.get_pos()[0])


class App:
    def __init__(self):
        pygame.init()
        self.res = self.width, self.height = (settings.WIDTH,
                                              settings.HEIGHT)
        self.screen = pygame.display.set_mode(self.res)
        self.clock = pygame.time.Clock()
        self.fps = settings.FPS
        self.app_name = settings.NAME
        self.bg_color = settings.bg_color
        self.pygame_icon = pygame.image.load('media/icon.ico')
        self.quit_event = pygame.event.Event(pygame.QUIT)
        self.player = Player(self)
        self.dwall = Dwall(self)

    def app_caption(self, mode='menu'):
        current_fps = self.clock.get_fps()
        if mode == 'game':
            pygame.display.set_caption(f'{self.app_name}. '
                                       f'Попытки: {self.player.health}. '
                                       f'Очки: {self.player.score}. '
                                       f'FPS: {current_fps:.2f}')
        if mode == 'menu':
            pygame.display.set_caption(f'{self.app_name}. '
                                       f'FPS: {current_fps:.2f}')

    def update(self, delta_t):
        self.player.update(delta_t)
        self.dwall.update(delta_t)

    def draw(self):
        self.player.draw()
        self.dwall.draw()
        ui.ui_game(self.screen, self.player)
        pygame.display.update()

    def start_menu(self):
        pygame.event.post(pygame.event.Event(settings.START_MENU))
        variables.SESSION_STAGE = 'START_MENU'

        in_menu = True
        while in_menu:
            delta_t = self.clock.tick(15) * 0.001 * 60

            pygame.display.set_icon(self.pygame_icon)

            event_handler()

            self.screen.fill(self.bg_color)

            self.player.update(delta_t)

            key = pygame.key.get_pressed()
            if key[settings.START_1] and key[settings.START_2]:
                pygame.event.post(pygame.event.Event(settings.START_TRAIN))
                variables.SESSION_STAGE = 'START_TRAIN'
                in_menu = False

            ui.ui_menu(self.screen)

            pygame.display.update()

            self.app_caption('menu')

    def warmup(self):
        start_ticks = pygame.time.get_ticks()
        while True:
            self.screen.fill(self.bg_color)

            self.player.draw()
            ui.ui_game(self.screen, self.player)

            seconds = (settings.warmup_time -
                       (pygame.time.get_ticks() - start_ticks) * 0.001)

            draw_sec = base2.render(f'{seconds:.2f}', True, settings.dark_grey)
            draw_sec_width = draw_sec.get_width()
            self.screen.blit(draw_sec,
                             (settings.WIDTH // 2 - draw_sec_width * .5,
                              settings.HEIGHT // 2))

            if seconds <= 0.03:
                break

            pygame.display.update()

            self.clock.tick(30)

        variables.is_warmuped = True
        variables.start_stage_time = dt.now()
        variables.pl_pos_log = True
        pygame.time.set_timer(settings.PLAYER_POS, settings.PLPOSLOG_TIMER)

    def game(self, delta_t):

        self.screen.fill(self.bg_color)

        if not variables.is_warmuped:
            self.warmup()

        self.update(delta_t)
        self.draw()

        self.app_caption('game')

    def pre_exam(self):

        in_pre_exam = True
        while in_pre_exam:
            delta_t = self.clock.tick(15) * 0.001 * 60

            event_handler()

            self.screen.fill(self.bg_color)

            self.player.update(delta_t)

            key = pygame.key.get_pressed()
            if key[settings.START_1] and key[settings.START_2]:
                pygame.event.post(pygame.event.Event(settings.START_EXAM))
                variables.SESSION_STAGE = 'START_EXAM'
                in_pre_exam = False

            ui.ui_pre_exam(self.screen)

            pygame.display.update()

            self.app_caption()

    def result(self):
        pygame.event.post(pygame.event.Event(settings.RESULT))

        in_result = True
        while in_result:
            delta_t = self.clock.tick(15) * 0.001 * 60

            event_handler()

            self.screen.fill(self.bg_color)

            self.player.update(delta_t)

            key = pygame.key.get_pressed()
            if key[settings.EXIT] or key[settings.CONTINUE]:
                in_result = False

            ui.ui_result(self.screen)

            pygame.display.update()

            self.app_caption()

        pygame.event.post(self.quit_event)
        event_handler()

    def run(self):

        self.start_menu()

        while True:
            delta_t = self.clock.tick(self.fps) * 0.001 * 60

            event_handler()

            if variables.SESSION_STAGE == 'RESULT':
                break

            if variables.SESSION_STAGE == 'START_EXAM':
                self.game(delta_t)
                self.player.log_player_pos()

            if variables.SESSION_STAGE == 'PRE_EXAM':
                self.pre_exam()

            if variables.SESSION_STAGE == 'START_TRAIN':
                self.game(delta_t)
                self.player.log_player_pos()

        self.result()


if __name__ == '__main__':
    app = App()
    app.run()
