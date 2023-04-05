import pygame

import settings
from player import Player
from dwall import Dwall
from debug import debug
# debug(info, pygame.mouse.get_pos()[1], pygame.mouse.get_pos()[0])


class App:
    def __init__(self):
        self.res = self.width, self.height = (settings.WIDTH,
                                              settings.HEIGHT)
        self.screen = pygame.display.set_mode(self.res)
        self.clock = pygame.time.Clock()
        self.fps = settings.FPS
        self.app_name = settings.NAME
        self.bg_color = settings.bg_color
        self.quit_event = pygame.event.Event(pygame.QUIT)
        self.player = Player(self)
        self.dwall = Dwall(self)

    def update(self):
        self.player.update()
        self.dwall.update()
        debug(self.dwall.dwall_list_previous)
        debug(self.player.health, 30)
        debug(self.player.score, 50)

    def draw(self):
        self.player.draw()
        self.dwall.draw()
        pygame.display.flip()

    def run(self):
        while True:
            [exit() for i in pygame.event.get() if i.type == pygame.QUIT]

            self.screen.fill(self.bg_color)

            self.update()
            self.draw()

            self.clock.tick(self.fps)
            current_fps = self.clock.get_fps()
            pygame.display.set_caption(f'{self.app_name}. '
                                       f'Health: {self.player.health}. '
                                       f'Score: {self.player.score}. '
                                       f'FPS: {current_fps:.2f}')


if __name__ == '__main__':
    app = App()
    app.run()
