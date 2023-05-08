import pygame

import settings
import variables
from player import Player
from dwall import Dwall
from debug import debug
from event_manager import (
    event_handler,
    START_MENU, START_TRAIN, START_EXAM, RESULT)
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
        self.screen.blit(
            self.font.render(variables.SESSION_STAGE, True, 'black'),
            (settings.WIDTH // 2, 10))
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
            if key[pygame.K_w] and key[pygame.K_UP]:
                pygame.event.post(pygame.event.Event(START_TRAIN))
                variables.SESSION_STAGE = 'START_TRAIN'
                in_menu = False

            self.screen.blit(
                self.font.render(variables.SESSION_STAGE, True, 'black'),
                (settings.WIDTH // 2, 10))

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
            if key[pygame.K_w] and key[pygame.K_UP]:
                pygame.event.post(pygame.event.Event(START_EXAM))
                variables.SESSION_STAGE = 'START_EXAM'
                in_pre_exam = False

            self.screen.blit(
                self.font.render(variables.SESSION_STAGE, True, 'black'),
                (settings.WIDTH // 2, 10),
            )

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
            if key[pygame.K_RETURN] or key[pygame.K_ESCAPE]:
                in_result = False

            self.screen.blit(
                self.font.render("RESULTS",
                                 True,
                                 'black'),
                (settings.WIDTH // 2, 10),
            )

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
            debug(self.player.score, 250)
            debug(variables.dwall_speed, 270)
            debug(variables.dwall_difficulty, 290)

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

            if variables.SESSION_STAGE == 'PRE_EXAM':
                self.pre_exam()

            if variables.SESSION_STAGE == 'START_EXAM':
                self.exam(delta_t)
                self.player.log_player_pos()

            if variables.SESSION_STAGE == 'RESULT':
                break

        self.result()


if __name__ == '__main__':
    app = App()
    app.run()
