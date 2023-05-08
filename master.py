"""
Game 1.
Author: Nikita Mashkov
Github: https://github.com/nmashkov
2023
"""
import pygame

import settings
import variables
from player import Player
from dwall import Dwall
from debug import debug
from event_manager import (
    event_handler,
    START_MENU, START_TRAIN, START_EXAM, RESULT)
import ui
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
        self.font = pygame.font.Font(None, 30)
        self.quit_event = pygame.event.Event(pygame.QUIT)
        self.player = Player(self)
        self.dwall = Dwall(self)

    def app_caption(self, mode='menu'):
        current_fps = self.clock.get_fps()
        if mode == 'game':
            pygame.display.set_caption(f'{self.app_name}. '
                                       f'Health: {self.player.health}. '
                                       f'Score: {self.player.score}. '
                                       f'FPS: {current_fps:.2f}')
        if mode == 'menu':
            pygame.display.set_caption(f'{self.app_name}. '
                                       f'FPS: {current_fps:.2f}')

    def update(self, delta_t):
        self.player.update(delta_t)
        self.dwall.update(delta_t)
        debug(self.dwall.dwall_list_previous)
        debug(self.player.health, 30)
        debug(self.player.score, 50)
        debug(self.dwall.dwall_amount, 70)
        debug(self.dwall.dwall_speed, 90)
        debug(self.dwall.difficulty, 110)

    def draw(self):
        self.player.draw()
        self.dwall.draw()
        ui.ui_game(self.screen, self.font)
        pygame.display.update()

    def start_menu(self):
        pygame.event.post(pygame.event.Event(START_MENU))
        variables.SESSION_STAGE = 'START_MENU'

        in_menu = True
        while in_menu:
            delta_t = self.clock.tick(15) / 1000 * 60

            event_handler()

            self.screen.fill(self.bg_color)

            self.player.update(delta_t)

            key = pygame.key.get_pressed()
            if key[settings.START_1] and key[settings.START_2]:
                pygame.event.post(pygame.event.Event(START_TRAIN))
                variables.SESSION_STAGE = 'START_TRAIN'
                in_menu = False

            ui.ui_menu(self.screen, self.font)

            pygame.display.update()

            self.app_caption('menu')

    def train(self, delta_t):

        self.screen.fill(self.bg_color)

        self.update(delta_t)
        self.draw()

        self.app_caption('game')

    def pre_exam(self):

        in_pre_exam = True
        while in_pre_exam:
            delta_t = self.clock.tick(15) / 1000 * 60

            event_handler()

            self.screen.fill(self.bg_color)

            self.player.update(delta_t)

            key = pygame.key.get_pressed()
            if key[settings.START_1] and key[settings.START_2]:
                pygame.event.post(pygame.event.Event(START_EXAM))
                variables.SESSION_STAGE = 'START_EXAM'
                in_pre_exam = False

            ui.ui_pre_exam(self.screen, self.font)

            pygame.display.update()

            self.app_caption(mode='game')

    def exam(self, delta_t):

        self.screen.fill(self.bg_color)

        self.update(delta_t)
        self.draw()

        self.app_caption('game')

    def result(self):
        pygame.event.post(pygame.event.Event(RESULT))

        in_result = True
        while in_result:
            delta_t = self.clock.tick(15) / 1000 * 60

            event_handler()

            self.screen.fill(self.bg_color)

            self.player.update(delta_t)

            key = pygame.key.get_pressed()
            if key[settings.EXIT] or key[settings.CONTINUE]:
                in_result = False

            ui.ui_result(self.screen, self.font)

            pygame.display.update()

            self.app_caption()

        pygame.event.post(self.quit_event)
        event_handler()

    def run(self):

        self.start_menu()

        while True:
            delta_t = self.clock.tick(self.fps) / 1000 * 60

            event_handler()

            if variables.SESSION_STAGE == 'START_TRAIN':
                self.train(delta_t)
                self.player.log_player_pos()

            if variables.SESSION_STAGE == 'START_EXAM':
                self.exam(delta_t)
                self.player.log_player_pos()

            if variables.SESSION_STAGE == 'PRE_EXAM':
                self.pre_exam()

            if variables.SESSION_STAGE == 'RESULT':
                break

        self.result()


if __name__ == '__main__':
    app = App()
    app.run()
