

import pygame
import spriteLoad
from helpers import *


class Sircull(spriteLoad.Sprite):
    def __init__(self, centerPoint, image):

        spriteLoad.Sprite.__init__(self, centerPoint, image)
        self.pellets = 0
        self.x_dist = 1
        self.y_dist = 1
        self.xMove = 0
        self.yMove = 0

    def MoveKeyDown(self, key):
        if (key == K_RIGHT):
            self.xMove += self.x_dist
        elif (key == K_LEFT):
            self.xMove += -self.x_dist
        elif (key == K_UP):
            self.yMove += -self.y_dist
        elif (key == K_DOWN):
            self.yMove += self.y_dist

    def MoveKeyUp(self, key):
        if (key == K_RIGHT):
            self.xMove += -self.x_dist
        elif (key == K_LEFT):
            self.xMove += self.x_dist
        elif (key == K_UP):
            self.yMove += self.y_dist
        elif (key == K_DOWN):
            self.yMove += -self.y_dist

    def update(self, block_group):
        self.rect.move_ip(self.xMove, self.yMove)
        if pygame.sprite.spritecollide(self, block_group, False):
            self.rect.move_ip(-self.xMove, -self.yMove)