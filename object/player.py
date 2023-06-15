import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, group, pos):
        super().__init__(group)

        self.image = pygame.Surface((32, 32))
        self.image.fill('green')
        self.rect = self.image.get_rect(center=pos)
