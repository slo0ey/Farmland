from scene.base import BaseScene

import pygame


class FarmScene(BaseScene):
    def __init__(self):
        super().__init__()

        self.world = pygame.sprite.LayeredDirty()
