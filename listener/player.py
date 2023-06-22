from event.entity import EntityEvent, EntityKeyDownEvent, EntityKeyUpEvent
from util.physics import get_direction4

import pygame


class PlayerEventListener:
    @staticmethod
    def on_frame(event: EntityEvent):
        player = event.entity

        player.position += player.velocity

    @staticmethod
    def on_keydown(event: EntityKeyDownEvent):
        player = event.entity
        dt = event.dt
        keys = event.keys

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

    @staticmethod
    def on_keyup(event: EntityKeyUpEvent):
        player = event.entity

        player.status = f"idle-{get_direction4(player.direction)}"
        player.velocity = pygame.Vector2(0, 0)
