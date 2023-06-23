from reactivex.operators import map

from core.rx import Rx
from entity.player import IPlayer
from event.entity import EntityEvent, EntityKeyDownEvent, EntityKeyUpEvent
from listener.player import PlayerEventListener
from sprite.player import PlayerSprite
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
        self._frame = Rx.frame.pipe(
            map(lambda event: EntityEvent(
                dt=event.dt,
                entity=self
            ))
        )
        self._keydown = Rx.keydown.pipe(
            map(lambda event: EntityKeyDownEvent(
                dt=event.dt,
                keys=event.keys,
                entity=self
            ))
        )
        self._keyup = Rx.keyup.pipe(
            map(lambda event: EntityKeyUpEvent(
                dt=event.dt,
                keys=event.keys,
                entity=self
            ))
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
        self._frame.subscribe(on_next=PlayerEventListener.on_frame)
        self._keydown.subscribe(on_next=PlayerEventListener.on_keydown)
        self._keyup.subscribe(on_next=PlayerEventListener.on_keyup)

    def end(self):
        self._frame.dispose()
        self._keydown.dispose()
        self._keyup.dispose()
