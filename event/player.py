from event import FrameEvent
from entity import Player

from dataclasses import dataclass

import pygame


@dataclass
class PlayerEvent(FrameEvent):
    player: Player


@dataclass
class PlayerKeyDownEvent(PlayerEvent):
    keys: pygame.key.ScancodeWrapper


@dataclass
class PlayerKeyUpEvent(PlayerEvent):
    keys: pygame.key.ScancodeWrapper


@dataclass
class PlayerAnimateEvent(PlayerEvent):
    pass


@dataclass
class PlayerSpriteUpdateEvent(PlayerEvent):
    pass
