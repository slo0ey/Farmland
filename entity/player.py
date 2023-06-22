from entity import BaseEntity
from entity.status import PlayerStatus
from sprite import BaseSprite
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
