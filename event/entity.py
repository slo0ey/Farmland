from event import FrameEvent
from entity import BaseEntity

from dataclasses import dataclass
from typing import TypeVar

import pygame


E = TypeVar('E', bound=BaseEntity)


@dataclass
class EntityEvent(FrameEvent):
    entity: E


@dataclass
class EntityKeyDownEvent(EntityEvent):
    keys: pygame.key.ScancodeWrapper


@dataclass
class EntityKeyUpEvent(EntityEvent):
    keys: pygame.key.ScancodeWrapper
