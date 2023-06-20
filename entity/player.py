from util.image import load_sprite
from util.physics import get_direction4
from util.types import Position

import pygame


class PlayerEngine:
    def __init__(
            self,
            start_pos: Position,
            start_direction: pygame.math.Vector2 = pygame.math.Vector2(0, 1),
            speed: int = 100,
    ):
        # general setup
        self.status = 'stand'

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


class Player(pygame.sprite.Sprite):
    def __init__(self, group, engine: PlayerEngine):
        super().__init__(group)
        self.engine = engine

        self.__animations = {
            'stand': [],
            'walk-up': [],
            'walk-down': [],
            'walk-left': [],
            'walk-right': [],
            'idle-up': [],
            'idle-down': [],
            'idle-left': [],
            'idle-right': [],
        }

        for anim in self.__animations.keys():
            for sprite in load_sprite('entity', ['player', anim]):
                self.__animations[anim].append(pygame.transform.scale(sprite, (96, 96)))

        self.image = self.__animations[self.engine.status][0]
        self.rect = self.image.get_rect(center=engine.position)
        self.frame = 0

    def animate(self, delta_time, transition_speed=1):
        total_frames = len(self.__animations[self.engine.status])
        self.frame += total_frames * delta_time * transition_speed

        if self.frame >= total_frames:
            self.frame = 0

        self.image = self.__animations[self.engine.status][int(self.frame)]
        self.rect.center = self.engine.position

    def update(self, delta_time):
        self.engine.on_keypress(delta_time)
        self.animate(delta_time)
