import pygame


def get_direction4(direction: pygame.math.Vector2):
    dir4 = ''
    if direction.y < 0:
        dir4 = 'UP'
    elif direction.y > 0:
        dir4 = 'DOWN'

    if direction.x < 0:
        dir4 = 'LEFT'
    elif direction.x > 0:
        dir4 = 'RIGHT'

    return dir4
