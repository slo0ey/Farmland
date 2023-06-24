from entity.player import IPlayer
from event.entity import EntityEvent, EntityKeyDownEvent, EntityKeyUpEvent

import pygame


def on_frame(event: EntityEvent):
    (dt, player) = event.unpack()
    keys = pygame.key.get_pressed()
    player: IPlayer = player

    if player.can_move():
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
            player.direction = vector.normalize()
            player.move(player.direction * player.speed * dt)
        else:
            player.idle()

        player.position += player.velocity


def on_keydown(event: EntityKeyDownEvent):
    (dt, keys, player) = event.unpack()
    player: IPlayer = player

    if player.status.is_on_tool():
        pass

    else:
        if keys[pygame.K_SPACE]:
            player.stop()
            player.hoe()


def on_keyup(event: EntityKeyUpEvent):
    (dt, keys, player) = event.unpack()
    player: IPlayer = player

    if player.status.is_on_tool():
        pass
