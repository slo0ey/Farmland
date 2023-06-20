from util.types import IntPosition
from os import walk

import pygame

__asset = './asset/'


class SpriteSheet:
    def __init__(
            self,
            filepath: str,
            rows: int,
            columns: int,
            width: int = 32,
            height: int = 32
    ):
        self.sheet = pygame.image.load(f"./asset/image/{filepath}")
        self.rows = rows
        self.columns = columns
        self.width = width
        self.height = height

    def sprite_at(
            self,
            position: IntPosition
    ) -> pygame.Surface:
        area = pygame.rect.Rect(
            left=position[1] * self.width,
            top=position[0] * self.height,
            width=self.width,
            height=self.height
        )
        image = pygame.Surface(area.size).convert_alpha()
        image.blit(self.sheet, (0, 0), area)

        return image

    def sprites_at(
            self,
            position_list: list[IntPosition]
    ) -> list[pygame.Surface]:
        return [self.sprite_at(pos) for pos in position_list]

    def sprites_to_dict(
            self,
            entries: list[tuple[str, IntPosition]]
    ) -> dict[str, pygame.Surface]:
        return {k: self.sprite_at(pos) for k, pos in entries}


def load_sprite(
        folder: str | list[str],
        prefix: str | list[str] = '',
        extension: str = '.png'
) -> list[pygame.Surface]:
    sprites = []
    if type(folder) is list:
        folder = '/'.join(folder)

    if type(prefix) is list:
        prefix = '-'.join(prefix)

    path = f"{__asset}/image/{folder}/"
    for _, __, files in walk(path):
        for image in files:
            if image.startswith(prefix) and image.endswith(extension):
                sprites.append(pygame.image.load(path + image).convert_alpha())

    return sprites
