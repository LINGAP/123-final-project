import pygame
from helpers import load_image
import random

class Enemy(pygame.sprite.Sprite):
    def __init__(self,image=None):
        super(Enemy, self).__init__()
        self.speed = random.randint(5, 20)
        if image == None:
            self.image, self.rect = load_image("Boximus.png",-1)
        else:
            self.image = image
            self.rect = image.get_rect(center=(520,random.randint(100,575)))

    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()




