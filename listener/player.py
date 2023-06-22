from event import PlayerKeyDownEvent, PlayerKeyUpEvent
from util.physics import get_direction4

import pygame


class PlayerEventListener:
    @staticmethod
    def on_keydown(event: PlayerKeyDownEvent):
        player = event.player
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
            player.position = player.direction * player.speed * dt
        else:
            player.status = f"idle-{get_direction4(player.direction)}"

    @staticmethod
    def on_keyup(event: PlayerKeyUpEvent):
        pass
