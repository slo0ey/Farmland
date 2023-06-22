from entity import BaseEntity

import pygame


class BaseSpriteFeature:
    def update(self, entity: BaseEntity, dt: float):
        pass


class BaseSprite(BaseSpriteFeature, pygame.sprite.Sprite):
    def __init__(self, group: pygame.sprite.AbstractGroup):
        super().__init__(group)


class BaseDirtySprite(BaseSpriteFeature, pygame.sprite.DirtySprite):
    def __init__(self, group: pygame.sprite.AbstractGroup):
        super().__init__(group)


class BaseWeakSprite(BaseSpriteFeature, pygame.sprite.WeakSprite):
    def __init__(self, group: pygame.sprite.AbstractGroup):
        super().__init__(group)


class BaseWeakDirtySprite(BaseSpriteFeature, pygame.sprite.WeakDirtySprite):
    def __init__(self, group: pygame.sprite.AbstractGroup):
        super().__init__(group)
