from sprite.base import BaseDirtySprite
from util.image import SpriteSheet
from util.types import Position

import pygame


class PlainTile(BaseDirtySprite):
    spritesheet = SpriteSheet('terrain/plain.png', rows=1, columns=15, width=64, height=64)

    def __init__(self, group, position: Position, rotate):
        super().__init__(group)
