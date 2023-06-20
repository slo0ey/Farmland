from controller.player import PlayerController, PlayerStatus
from util.image import SpriteSheet

import pygame

# TODO : SpriteSheet 로 교체
class Player(pygame.sprite.Sprite):
    def __init__(self, group, controller: PlayerController):
        super().__init__(group)

        self.controller = controller
        self.spritesheet = SpriteSheet('entity/player.png', rows=1, columns=21, width=64, height=64)
        self.__animations = {}

        self.__animations[PlayerStatus.STAND] = self.spritesheet.sprites_at([(0, 0)])

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
