from event.base import FrameEvent
from entity.base import BaseEntity

from dataclasses import dataclass
from typing import TypeVar

import pygame


E = TypeVar('E', bound=BaseEntity)


@dataclass
class EntityEvent(FrameEvent):
    entity: E

    def unpack(self):
        return self.dt, self.entity


@dataclass
class EntityKeyDownEvent(EntityEvent):
    keys: pygame.key.ScancodeWrapper

    def unpack(self):
        return self.dt, self.entity, self.keys


@dataclass
class EntityKeyUpEvent(EntityEvent):
    keys: pygame.key.ScancodeWrapper

    def unpack(self):
        return self.dt, self.entity, self.keys
