import sys
from random import randint

import pygame
from pygame.sprite import Group

from raindrop import Raindrop

def run():
    pygame.init()
    screen = pygame.display.set_mode((600, 600))
    pygame.display.set_caption('Rain Drops')
    
    raindrops = Group()

    available_screen_width = screen.get_rect().width - Raindrop().rect.width * 2

    num_raindrops = int(available_screen_width / (Raindrop().rect.width * 2))

    for raindrop_num in range(4):
        raindrop = Raindrop()
        raindrop.rect.left = randint(0, available_screen_width)
        raindrops.add(raindrop)

    i = 0
    while True:
        i += 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    sys.exit()

        screen.fill((255, 255, 255))
        raindrops.update()
        for raindrop in raindrops.copy():
            if raindrop.rect.top > screen.get_rect().bottom:
                raindrops.remove(raindrop)
        if not i % 10:
            raindrop = Raindrop()
            raindrop.rect.left = randint(0, available_screen_width)
            raindrops.add(raindrop)
        raindrops.draw(screen)
        pygame.display.flip()

run()