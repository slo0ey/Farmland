from util.types import Position

import pygame


class BaseEntity:
    def __init__(
            self,
            position: Position,
            direction: pygame.Vector2,
            sprite: pygame.sprite.Sprite
    ):
        self.position = position
        self.direction = direction
        self.velocity = pygame.Vector2(0, 0)
        self.sprite = sprite

    def start(self):
        pass

    def end(self):
        pass
