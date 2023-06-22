from reactivex.operators import map

from entity import IPlayer
from event import EntityKeyDownEvent, EntityKeyUpEvent
from listener import PlayerEventListener
from main import GAME
from sprite import PlayerSprite
from util.types import Position

import pygame


class Player(IPlayer):
    def __init__(
            self,
            position: Position,
            direction: pygame.Vector2,
            sprite: PlayerSprite
    ):
        super().__init__(position, direction, sprite)

        # Rx event setup
        self._keydown = GAME.keydown.pipe(
            map(lambda dt: EntityKeyDownEvent(dt, self, pygame.key.get_pressed()))
        )
        self._keyup = GAME.keyup.pipe(
            map(lambda dt: EntityKeyUpEvent(dt, self, pygame.key.get_pressed()))
        )

    @staticmethod
    def create(
            position: Position,
            direction: pygame.Vector2,
            sprite_group: pygame.sprite.AbstractGroup
    ) -> IPlayer:
        return Player(
            position=position,
            direction=direction,
            sprite=PlayerSprite(
                group=sprite_group,
                position=position
            )
        )

    def start(self):
        self._keydown.subscribe(on_next=PlayerEventListener.on_keydown)
        self._keyup.subscribe(on_next=PlayerEventListener.on_keyup)

    def end(self):
        self._keydown.dispose()
        self._keyup.dispose()
