from entity.base import BaseEntity
from entity.status.player import PlayerStatus
from sprite.base import BaseSprite
from util.types import Position

import pygame


class IPlayer(BaseEntity):
    def __init__(
            self,
            position: Position,
            direction: pygame.Vector2,
            sprite: BaseSprite,
    ):
        super().__init__(position, direction, sprite)

        # General setup
        self.status = PlayerStatus.STAND
        self.speed = 100

    def idle(self):
        pass

    def move(self):
        pass

    def hoe(self):
        pass

    def plant(self):
        pass

    def watering(self):
        pass

    def harvest(self):
        pass

    def axe(self):
        pass
