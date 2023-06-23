from event.base import *
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
class EntityKeyDownEvent(KeyDownEvent, EntityEvent):
    def unpack(self):
        return self.dt, self.keys, self.entity


@dataclass
class EntityKeyUpEvent(KeyUpEvent, EntityEvent):
    def unpack(self):
        return self.dt, self.keys, self.entity


@dataclass
class EntityMouseDownEvent(MouseDownEvent, EntityEvent):
    def unpack(self):
        return self.dt, self.entity


@dataclass
class EntityMouseUpEvent(MouseUpEvent, EntityEvent):
    def unpack(self):
        return self.dt, self.entity
