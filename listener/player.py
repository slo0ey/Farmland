from reactivex import timer

from entity.player import IPlayer
from event.entity import EntityEvent, EntityKeyDownEvent, EntityKeyUpEvent
from util.physics import get_direction4

import pygame


class PlayerEventListener:
    @staticmethod
    def on_frame(event: EntityEvent):
        player: IPlayer = event.entity

        player.position += player.velocity

    @staticmethod
    def on_keydown(event: EntityKeyDownEvent):
        (dt, keys, player) = event.unpack()

        PlayerEventListener._update_velocity(dt, keys, player)

    @staticmethod
    def on_keyup(event: EntityKeyUpEvent):
        (dt, keys, player) = event.unpack()

        PlayerEventListener._update_velocity(dt, keys, player)

    @staticmethod
    def _update_velocity(
            dt: float,
            keys: pygame.key.ScancodeWrapper,
            player: IPlayer
    ):
        vector = pygame.Vector2(0, 0)

        if keys[pygame.K_w]:
            vector.y += -1
        if keys[pygame.K_s]:
            vector.y += 1
        if keys[pygame.K_a]:
            vector.x += -1
        if keys[pygame.K_d]:
            vector.x += 1

        if vector.magnitude() > 0:
            player.status = f"walk-{get_direction4(vector)}"
            player.direction = vector.normalize()
            player.velocity = player.direction * player.speed * dt
        else:
            player.status = f"idle-{get_direction4(player.direction)}"
            player.velocity = pygame.Vector2(0, 0)
