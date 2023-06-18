import pygame


def get_direction4(direction: pygame.math.Vector2):
    dir4 = ''
    if direction.y < 0:
        dir4 = 'up'
    elif direction.y > 0:
        dir4 = 'down'

    if direction.x < 0:
        dir4 = 'left'
    elif direction.x > 0:
        dir4 = 'right'

    return dir4
