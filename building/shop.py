from util.image import load_sprite

import pygame


class Shop(pygame.sprite.Sprite):
    def __init__(self, group, spawn_pos):
        super().__init__(group)

        self.image = pygame.transform.scale(load_sprite('building', 'shop')[0], (384, 256))
        self.rect = self.image.get_rect(center=spawn_pos)

    def update(self, dt):
        pass
