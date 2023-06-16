import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, group, pos):
        super().__init__(group)

        self.image = pygame.Surface((32, 32))
        self.image.fill('green')
        self.rect = self.image.get_rect(center=pos)
        self.direction = pygame.math.Vector2(0, 0)
        self.position = pygame.math.Vector2(self.rect.center)
        self.speed = 400

    def input(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            self.direction.y = -1
        elif keys[pygame.K_DOWN]:
            self.direction.y = 1
        else:
            self.direction.y = 0

        if keys[pygame.K_LEFT]:
            self.direction.x = -1
        elif keys[pygame.K_RIGHT]:
            self.direction.x = 1
        else:
            self.direction.x = 0

    def move(self, dt):
        if self.direction.magnitude() > 0:
            self.direction = self.direction.normalize()
        self.position += self.direction * self.speed * dt
        self.rect.center = self.position

    def update(self, dt):
        self.input(dt)
        self.move(dt)
