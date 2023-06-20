from entity.player import Player, PlayerController
from building.shop import Shop

import pygame


class FarmWorld:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()
        self.all_sprites = pygame.sprite.Group()

        self.shop = Shop(self.all_sprites, (640, 360))
        self.player = Player(self.all_sprites, PlayerController(start_pos=(684, 610)))

    def run(self, dt):
        self.display_surface.fill('#E3FF98')
        self.all_sprites.draw(self.display_surface)
        self.all_sprites.update(dt)
