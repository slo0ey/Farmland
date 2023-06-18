from os import walk
import pygame

__asset = './asset/'


def load_sprite(
        target: str | list[str],
        prefix: str | list[str] = '',
        extension: str = '.png'
) -> list[pygame.surface.Surface]:
    sprites = []
    if type(target) is list:
        target = '/'.join(target)

    if type(prefix) is list:
        prefix = '-'.join(prefix)

    path = f"{__asset}/image/{target}/"
    for _, __, files in walk(path):
        for image in files:
            if image.startswith(prefix) and image.endswith(extension):
                sprites.append(pygame.image.load(path + image).convert_alpha())

    return sprites
