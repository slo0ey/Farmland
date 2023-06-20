from util.physics import get_direction4
from util.types import Position, Status

import pygame


class PlayerStatus(Status):
    STAND = 'stand'
    WALK_UP = 'walk-up'
    WALK_DOWN = 'walk-down'
    WALK_LEFT = 'walk-left'
    WALK_RIGHT = 'walk-right'
    IDLE_UP = 'idle-up'
    IDLE_DOWN = 'idle-down'
    IDLE_LEFT = 'idle-left'
    IDLE_RIGHT = 'idle-right'


class PlayerController:
    def __init__(
            self,
            start_pos: Position,
            start_direction: pygame.math.Vector2 = pygame.math.Vector2(0, 1),
            speed: int = 100,
    ):
        # general setup
        self.status = PlayerStatus.STAND

        # physics setup
        self.position = start_pos
        self.direction = start_direction
        self.speed = speed

    def on_keypress(self, delta_time):
        keys = pygame.key.get_pressed()

        self.on_keypress_wasd(keys, delta_time)

    # keypress events
    def on_keypress_wasd(self, keys: pygame.key.ScancodeWrapper, delta_time):
        vector = pygame.math.Vector2(0, 0)

        if keys[pygame.K_w]:
            vector.y += -1
        if keys[pygame.K_s]:
            vector.y += 1
        if keys[pygame.K_a]:
            vector.x += -1
        if keys[pygame.K_d]:
            vector.x += 1

        if vector.magnitude() > 0:
            self.status = f"walk-{get_direction4(vector)}"
            self.direction = vector.normalize()
            self.position += self.direction * self.speed * delta_time
        else:
            self.status = f"idle-{get_direction4(self.direction)}"
