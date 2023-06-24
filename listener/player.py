from entity.player import IPlayer
from event.entity import EntityEvent, EntityKeyDownEvent, EntityKeyUpEvent
from util.physics import get_direction4

import pygame


def on_frame(event: EntityEvent):
    player: IPlayer = event.entity

    player.position += player.velocity


def on_keydown(event: EntityKeyDownEvent):
    (dt, keys, player) = event.unpack()
    player: IPlayer = player

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
        player.move()


def on_keyup(event: EntityKeyUpEvent):
    (dt, keys, player) = event.unpack()
    player: IPlayer = player

    if player.status.is_on_tool():
        return

    if keys[pygame.K_SPACE]:
        player.hoe()
    else:
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
            player.move()
