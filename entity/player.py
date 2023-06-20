from controller.player import PlayerController, PlayerStatus
from util.image import load_sprite

import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, group, controller: PlayerController):
        super().__init__(group)

        self.controller = controller
        self.__animations = {x: [] for x in PlayerStatus}

        for anim in self.__animations.keys():
            for sprite in load_sprite('entity', ['player', anim]):
                self.__animations[anim].append(pygame.transform.scale(sprite, (96, 96)))

        self.image = self.__animations[self.controller.status][0]
        self.rect = self.image.get_rect(center=controller.position)
        self.frame = 0

    def animate(self, delta_time, transition_speed=1):
        total_frames = len(self.__animations[self.controller.status])
        self.frame += total_frames * delta_time * transition_speed

        if self.frame >= total_frames:
            self.frame = 0

        self.image = self.__animations[self.controller.status][int(self.frame)]
        self.rect.center = self.controller.position

    def update(self, delta_time):
        self.controller.on_keypress(delta_time)
        self.animate(delta_time)
