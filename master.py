import pygame

import settings
import variables
from player import Player
from dwall import Dwall
from debug import debug
from event_manager import (
    event_handler,
    START_MENU, START_TRAIN)
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

    def draw(self):
        self.player.draw()
        self.dwall.draw()
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
            if key[pygame.K_RETURN]:
                pygame.event.post(pygame.event.Event(START_TRAIN))
                variables.SESSION_STAGE = 'START_TRAIN'
                in_menu = False

            self.screen.blit(
                self.font.render("GAME START MENU",
                                 True,
                                 'black'),
                (100, 100),
            )

            pygame.display.update()

            self.app_caption('menu')

    def run(self):

        self.start_menu()

        while True:
            delta_t = self.clock.tick(self.fps) / 1000 * 60

            event_handler()

            self.screen.fill(self.bg_color)

            self.update(delta_t)
            self.draw()

            self.app_caption('game')


if __name__ == '__main__':
    app = App()
    app.run()
