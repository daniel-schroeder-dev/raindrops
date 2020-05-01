from random import randint

import pygame
from pygame.sprite import Sprite

class Raindrop(Sprite):

    def __init__(self):
        super().__init__()

        self.image = pygame.image.load('./images/raindrop.jpg')
        self.rect = self.image.get_rect()
        self.rect.bottom = 0

        self.i = 0

    def update(self):
        self.i += 1
        if self.i % 3:
            self.rect.y += 1