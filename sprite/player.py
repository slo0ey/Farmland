from entity import IPlayer
from entity.status import PlayerStatus
from sprite import BaseSprite
from util.image import SpriteSheet
from util.types import Position


class PlayerSprite(BaseSprite):
    def __init__(self, group, position: Position):
        super().__init__(group)

        self.spritesheet = SpriteSheet('entity/player.png', rows=1, columns=21, width=64, height=64)
        self.animations = {
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

        self.image = self.animations[PlayerStatus.STAND][0]
        self.rect = self.image.get_rect(center=position)
        self.frame = 0
        self.previous_status = ''

    def update(self, player: IPlayer, dt: float):
        if self.previous_status != player.status:
            self.frame = 0
            self.previous_status = player.status
        else:
            total_frames = len(self.animations[player.status])
            self.frame += total_frames * dt

            if self.frame >= total_frames:
                self.frame = 0

        self.image = self.animations[player.status][int(self.frame)]
        self.rect.center = player.position
