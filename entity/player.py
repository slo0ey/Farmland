from controller.player import PlayerController, PlayerStatus
from util.image import SpriteSheet

import pygame


# TODO : SpriteSheet 로 교체
class Player(pygame.sprite.Sprite):
    def __init__(self, group, controller: PlayerController):
        super().__init__(group)

        self.controller = controller
        self.spritesheet = SpriteSheet('entity/player.png', rows=1, columns=21, width=64, height=64)
        self.__animations = self.init_sprites()

        self.image = self.__animations[self.controller.status][0]
        self.rect = self.image.get_rect(center=controller.position)
        self.frame = 0

    def init_sprites(self):
        return {
            PlayerStatus.IDLE_DOWN: self.spritesheet.sprites_at([(0, 0)]),
            PlayerStatus.IDLE_LEFT: self.spritesheet.sprites_at([(0, 1)]),
            PlayerStatus.IDLE_RIGHT: self.spritesheet.sprites_at([(0, 2)]),
            PlayerStatus.IDLE_UP: self.spritesheet.sprites_at([(0, 3)]),
            PlayerStatus.STAND: self.spritesheet.sprites_at([(0, 4)]),
            PlayerStatus.WALK_DOWN: self.spritesheet.sprites_at([(0, 5), (0, 6), (0, 7), (0, 8)]),
            PlayerStatus.WALK_LEFT: self.spritesheet.sprites_at([(0, 9), (0, 10), (0, 11), (0, 12)]),
            PlayerStatus.WALK_RIGHT: self.spritesheet.sprites_at([(0, 13), (0, 14), (0, 15), (0, 16)]),
            PlayerStatus.WALK_UP: self.spritesheet.sprites_at([(0, 17), (0, 18), (0, 19), (0, 20)])
        }

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
