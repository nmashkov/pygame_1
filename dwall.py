import pygame
from random import randrange as rnd

import settings


def dwall_new(dblock_w, dblock_h, dwall_list_previous, difficulty):
    done = False
    while not done:
        dwall_list = [i*rnd(0, 2) for i in range(11)]

        for i in range(1, len(dwall_list_previous)):
            if not dwall_list_previous[i]:
                dwall_list[i] = i

        if dwall_list == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
            dwall_list = [0, 0, 2, 3, 4, 5, 6, 7, 8, 9, 0]
        if dwall_list == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]:
            dwall_list = [0, 1, 0, 3, 4, 5, 6, 7, 8, 0, 10]

        counter = 0
        for i in dwall_list:
            if not i:
                counter += 1
        if counter < difficulty:
            done = True

    print(dwall_list)
    new_dwall = [pygame.Rect(70 * j - 70,
                             -70,
                             dblock_w,
                             dblock_h) for j in dwall_list]
    return new_dwall, dwall_list


class Dwall:
    def __init__(self, app):
        self.app = app
        self.player = self.app.player
        # dwall params
        self.dblock_w = settings.dblock_w
        self.dblock_h = settings.dblock_h
        self.dblock_color = settings.dblock_color
        self.dwall_speed = settings.dwall_speed
        # dwall utils
        self.dwall = []
        self.dwall_list_previous = []
        self.difficulty = settings.difficulty

    def draw(self):
        # drawing death wall
        [pygame.draw.rect(self.app.screen, self.dblock_color, dblock)
         for dblock in self.dwall]

    def update(self):
        # creating death wall
        if len(self.dwall) == 0:
            self.dwall, self.dwall_list_previous = dwall_new(
                self.dblock_w,
                self.dblock_h,
                self.dwall_list_previous,
                self.difficulty)

        # drawing checkline
        line = pygame.draw.line(self.app.screen,
                                (255, 255, 255),
                                [0, self.app.res[1]],
                                [self.app.res[0], self.app.res[1]],
                                3)

        # death wall moving and checks
        for dblock in self.dwall:
            dblock.y += self.dwall_speed

            collision_with_line = line.collidelistall(self.dwall)
            if len(collision_with_line) > 0:
                self.dwall = []
                self.player.score += 1
                break

            collisions = self.player.square.collidelistall(self.dwall)
            if len(collisions) > 0:
                print('Death')
                self.player.health -= 1
                if not self.player.health:
                    pygame.event.post(self.app.quit_event)
                self.dwall = []
                self.player.square.left = (self.app.res[0] // 2
                                           - self.player.square_w // 2)
                break
