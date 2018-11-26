import os, sys
import pygame
import random
import Level001
import spriteLoad
from sircullSprite import Sircull
from pygame.locals import *
from helpers import *

red = (150, 50, 50)
orange = (200, 100, 50)
yellow = (200, 175, 50)
green = (50, 150, 50)
blue = (50, 50, 150)
purple = (150, 50, 200)
WALL_SIZE = 24
resolution = (600, 800)


ADDENEMY= pygame.USEREVENT+1
pygame.time.set_timer(ADDENEMY,500)

class Game:
    def __init__(self, width=resolution[0], height=resolution[1]):

        pygame.init()

        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))

    def MainLoop(self):

        self.LoadSprites()
        self.background = pygame.Surface(self.screen.get_size())
        self.background = self.background.convert()
        self.background.fill((0, 0, 0))

        self.brick_sprites.draw(self.background)
        enemies = pygame.sprite.Group()
        health =0
        while 1:
            E = Enemy()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == KEYDOWN:
                    if ((event.key == K_RIGHT)
                        or (event.key == K_LEFT)
                        or (event.key == K_UP)
                        or (event.key == K_DOWN)):
                        self.sircull.MoveKeyDown(event.key)
                elif event.type == KEYUP:
                    if ((event.key == K_RIGHT)
                        or (event.key == K_LEFT)
                        or (event.key == K_UP)
                        or (event.key == K_DOWN)):
                        self.sircull.MoveKeyUp(event.key)
                elif (event.type == ADDENEMY):
                    new_enemy=E
                    enemies.add(new_enemy)


            self.sircull_sprites.update(self.brick_sprites)

            collone = pygame.sprite.spritecollide(self.sircull, self.powerup_sprites, True)
            if collone != 0:
                health += len(collone)

            self.sircull.points = self.sircull.points + len(collone)

            self.screen.blit(self.background, (0, 0))
            if pygame.font:
                font = pygame.font.Font(None, 30)
                text = font.render("Health %s" % self.sircull.points, 1, (50, 150, 50))
                textpos = text.get_rect(centerx=self.background.get_width() / 2)
                self.screen.blit(text, textpos)

            for attacker in enemies:
                attacker.update()
                self.screen.blit(attacker.image, attacker.rect)
                if pygame.sprite.spritecollideany(self.sircull,enemies) :
                    health -=1
                    self.sircull.points -=1
                    enemies.remove(attacker)
                    enemies.update()
                    print("-1 health! now health is", health)
                if health < 0:
                    self.sircull.kill()
                    print("Game Over")
                    sys.exit()

            self.powerup_sprites.draw(self.screen)
            self.sircull_sprites.draw(self.screen)
            self.quad_sprite.draw(self.screen)

            pygame.display.flip()

    def LoadSprites(self):

        x_offset = (WALL_SIZE / 2)
        y_offset = (WALL_SIZE / 2)

        firstlev = Level001.level()
        layout = firstlev.getLayout()
        img_list = firstlev.getSprites()

        self.powerup_sprites = pygame.sprite.Group()
        self.brick_sprites = pygame.sprite.Group()

        for y in range(len(layout)):
            for x in range(len(layout[y])):

                centerPoint = [(x * WALL_SIZE) + x_offset, (y * WALL_SIZE + y_offset)]
                if layout[y][x] == firstlev.BRICKS:
                    brick = spriteLoad.Sprite(centerPoint, img_list[firstlev.BRICKS])
                    self.brick_sprites.add(brick)
                elif layout[y][x] == firstlev.QUADRANGLE:
                    self.quadrangle = spriteLoad.Sprite(centerPoint, img_list[firstlev.QUADRANGLE])
                elif layout[y][x] == firstlev.POWERUP:
                    powerup = spriteLoad.Sprite(centerPoint, img_list[firstlev.POWERUP])
                    self.powerup_sprites.add(powerup)
                elif layout[y][x] == firstlev.SIRCULL:
                    self.sircull = Sircull(centerPoint, img_list[firstlev.SIRCULL])
                    self.sircull.points = 0

        self.sircull_sprites = pygame.sprite.RenderPlain((self.sircull))
        self.quad_sprite = pygame.sprite.RenderPlain((self.quadrangle))



class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()
        self.speed = random.randint(1,5)
        self.image, self.rect = load_image("Boximus.png",-1)
        self.rect = self.image.get_rect(center=(520,random.randint(200,575)))

    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()
            self.remove()


if __name__ == "__main__":
    gamescreen = Game(500, 575)
    gamescreen.MainLoop()

