from building.shop import Shop
from entity.impl.player import Player

import pygame


class FarmWorld:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()
        self.all_sprites = pygame.sprite.Group()
        self.player_sprite_group = pygame.sprite.GroupSingle()

        self.shop = Shop(self.all_sprites, (640, 360))
        self.player = Player.create(
            position=(640, 660),
            direction=pygame.Vector2(0, 1),
            sprite_group=self.player_sprite_group
        )

        self.player.start()

    def update(self, dt):
        self.display_surface.fill('#E3FF98')
        self.all_sprites.draw(self.display_surface)
        self.all_sprites.update(
            dt=dt
        )

        self.player_sprite_group.draw(self.display_surface)
        self.player_sprite_group.update(
            player=self.player,
            dt=dt
        )
