"""
Synergy-1
Author: Nikita Mashkov, Alexey Malishevsky
Programmer: Nikita Mashkov
Designer: Evgeny Manuylenko
Github: https://github.com/nmashkov
2023
"""
import pygame
from datetime import datetime as dt

import settings
import variables
from player import Player
from dwall import DwallGroup
from event_manager import event_handler
from fonts import base2, button as bt
import ui
from debug import debug
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
        # all sprites
        self.all_sprites = pygame.sprite.Group()
        # objects
        self.player = Player(self)
        self.dwall = DwallGroup(self)

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

    def debug_panel(self):
        debug(variables.dwall_speed, 'dwall_speed')
        debug(variables.dwall_difficulty, 'dwall_difficulty', 70)
        debug(variables.lp_active_time, 'lp_active_time', 90)
        debug(variables.lp_active_acc_time, 'lp_active_acc_time', 110)
        debug(variables.lp_key_pushes, 'lp_key_pushes', 130)
        debug(variables.rp_active_time, 'rp_active_time', 150)
        debug(variables.rp_active_acc_time, 'rp_active_acc_time', 170)
        debug(variables.rp_key_pushes, 'rp_key_pushes', 190)
        debug(variables.accelerate, 'accelerate', 210)
        debug(variables.accelerate_time, 'accelerate_time', 230)
        debug(variables.conflict, 'conflict', 250)
        debug(variables.conflict_time, 'conflict_time', 270)
        debug(variables.cooperation, 'cooperation', 290)
        debug(variables.cooperative_time, 'cooperative_time', 310)

    def update(self, delta_t):
        self.player.update(delta_t)
        self.dwall.update()
        if variables.debug_activated:
            self.debug_panel()

    def draw(self):
        self.all_sprites.draw(self.screen)
        ui.ui_game(self.screen, self.player)
        pygame.display.update()

    def button_in(self):
        top = 30
        clicked = False

        button = pygame.Rect(settings.WIDTH-top - 38, top*1+2, 36, 36)
        pygame.draw.rect(self.screen, settings.back1, button, border_radius=10)
        self.screen.blit(bt.render('i', True, (255, 255, 255)),  # 5
                         (settings.WIDTH-top-22, top*1+8))

        pos = pygame.mouse.get_pos()

        # check mouseover and clicked conditions
        if button.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and not clicked:
                clicked = True
                self.credits()

    def button_out(self):
        top = 30
        clicked = False
        in_credits = True

        button = pygame.Rect(settings.WIDTH-top - 38, top*1+2, 36, 36)
        pygame.draw.rect(self.screen, settings.back1, button, border_radius=10)
        self.screen.blit(bt.render('H', True, (255, 255, 255)),  # 15
                         (settings.WIDTH-top-27, top*1+8))

        pos = pygame.mouse.get_pos()

        # check mouseover and clicked conditions
        if button.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and not clicked:
                clicked = True
                in_credits = False

        return in_credits

    def credits(self):
        in_credits = True
        while in_credits:
            self.clock.tick(15)

            event_handler()

            self.screen.fill(self.bg_color)

            in_credits = self.button_out()

            key = pygame.key.get_pressed()
            if key[pygame.K_ESCAPE]:
                in_credits = False

            ui.ui_credits(self.screen)

            pygame.display.update()

            self.app_caption('menu')

    def start_menu(self):
        pygame.event.post(pygame.event.Event(settings.START_MENU))
        variables.SESSION_STAGE = 'START_MENU'

        in_menu = True
        while in_menu:
            delta_t = self.clock.tick(15) * 0.001 * 60

            pygame.display.set_icon(self.pygame_icon)

            event_handler()

            self.screen.fill(self.bg_color)

            self.button_in()

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

            self.all_sprites.draw(self.screen)
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

            if variables.debug_activated:
                self.debug_panel()

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

            if variables.debug_activated:
                self.debug_panel()

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

            elif variables.SESSION_STAGE == 'START_EXAM':
                self.game(delta_t)
                self.player.log_player_pos()

            elif variables.SESSION_STAGE == 'PRE_EXAM':
                self.pre_exam()

            elif variables.SESSION_STAGE == 'START_TRAIN':
                self.game(delta_t)
                self.player.log_player_pos()

        self.result()


if __name__ == '__main__':
    app = App()
    app.run()
