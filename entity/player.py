from util.image import load_sprite
from util.physics import get_direction4

import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, group, spawn_pos):
        super().__init__(group)

        # general setup
        self.status = 'stand'

        # sprite setup
        self.init_sprites()
        self.image = self.__animations[self.status][0]
        self.rect = self.image.get_rect(center=spawn_pos)
        self.frame = 0

        # physics setup
        self.vector = pygame.math.Vector2(0, 0)
        self.direction = pygame.math.Vector2(0, 1)
        self.position = pygame.math.Vector2(self.rect.center)
        self.speed = 120

    def init_sprites(self):
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

    def input(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            self.vector.y = -1
        elif keys[pygame.K_DOWN]:
            self.vector.y = 1
        else:
            self.vector.y = 0

        if keys[pygame.K_LEFT]:
            self.vector.x = -1
        elif keys[pygame.K_RIGHT]:
            self.vector.x = 1
        else:
            self.vector.x = 0

    def update_state(self):
        if self.vector.magnitude() > 0:
            self.direction = self.vector.normalize()
            self.status = f"walk-{get_direction4(self.direction)}"
        else:
            self.status = f"idle-{get_direction4(self.direction)}"

    def move(self, dt):
        if self.vector.magnitude() > 0:
            self.vector = self.vector.normalize()
        self.position += self.vector * self.speed * dt
        self.rect.center = self.position

    def animate(self, dt, speed=1):
        total_frames = len(self.__animations[self.status])
        self.frame += total_frames * dt * speed

        if self.frame >= total_frames:
            self.frame = 0

        self.image = self.__animations[self.status][int(self.frame)]

    def update(self, dt):
        self.input(dt)
        self.update_state()
        self.move(dt)
        self.animate(dt)
