from sprite.base import BaseDirtySprite
from util.image import SpriteSheet
from util.types import Position, LateInit

import pygame


class PlainTile(BaseDirtySprite):
    spritesheet: LateInit[SpriteSheet]

    def __init__(
            self,
            group,
            position: Position,
            plain_type: int = 0,
            rotate: int = 0
    ):
        super().__init__(group)

        if PlainTile.spritesheet is None:
            PlainTile.spritesheet = SpriteSheet('terrain/plain.png', rows=1, columns=15, width=64, height=64)

        self.image = self.spritesheet.sprite_at((0, plain_type))
        self.image = pygame.transform.rotate(self.image, rotate * 90)
        self.rect = self.image.get_rect()
        self.rect.center = position
        self.dirty = 2
