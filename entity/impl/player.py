from reactivex import timer
from reactivex.operators import map

from core.rx import Rx
from entity.player import IPlayer
from event.entity import EntityEvent, EntityKeyDownEvent, EntityKeyUpEvent
from listener.player import on_frame, on_keydown, on_keyup
from sprite.player import PlayerSprite
from util.physics import get_direction4
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
        self._frame.subscribe(on_next=on_frame)
        self._keydown.subscribe(on_next=on_keydown)
        self._keyup.subscribe(on_next=on_keyup)

    def end(self):
        self._frame.dispose()
        self._keydown.dispose()
        self._keyup.dispose()

    def idle(self):
        self.status = f"idle-{get_direction4(self.direction)}"
        self.velocity = pygame.Vector2(0, 0)

    def move(self):
        self.status = f"walk-{get_direction4(self.direction)}"
        self.velocity = self.direction * self.speed * (pygame.time.get_ticks() / 1000)

    def hoe(self):
        self.status = f"hoe-{get_direction4(self.direction)}"

        def on_complete():
            self.status = f"idle-{get_direction4(self.direction)}"

        timer(
            duetime=980,
            scheduler=Rx.get_scheduler()
        ).subscribe(
            on_completed=on_complete
        )
