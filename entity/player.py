from reactivex.operators import map

from event import PlayerKeyDownEvent, PlayerKeyUpEvent
from listener import PlayerEventListener
from sprite import PlayerSprite
from util.enums import PlayerStatus
from util.types import Position
from main import GAME

import pygame


class Player:
    def __init__(
            self,
            listener: PlayerEventListener,
            sprite: PlayerSprite,
            start_pos: Position,
            start_direction: pygame.Vector2,
    ):
        self.listener = listener
        self.sprite = sprite

        self.status = PlayerStatus.STAND
        self.position = start_pos
        self.direction = start_direction
        self.speed = 100

        # Rx event setup
        self.keydown_subs = GAME.keydown.pipe(
            map(lambda dt: PlayerKeyDownEvent(dt, self, pygame.key.get_pressed()))
        ).subscribe(
            on_next=self.listener.on_keydown
        )
        self.keyup_subs = GAME.keyup.pipe(
            map(lambda dt: PlayerKeyUpEvent(dt, self, pygame.key.get_pressed()))
        ).subscribe(
            on_next=self.listener.on_keyup
        )

    def remove(self):
        self.keydown_subs.dispose()
        self.keyup_subs.dispose()
