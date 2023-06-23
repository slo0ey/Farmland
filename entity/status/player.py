from .base import Status


class PlayerStatus(Status):
    STAND = 'stand'
    WALK_UP = 'walk-up'
    WALK_DOWN = 'walk-down'
    WALK_LEFT = 'walk-left'
    WALK_RIGHT = 'walk-right'
    IDLE_UP = 'idle-up'
    IDLE_DOWN = 'idle-down'
    IDLE_LEFT = 'idle-left'
    IDLE_RIGHT = 'idle-right'
    HOE_UP = 'hoe-up'
    HOE_DOWN = 'hoe-down'
    HOE_LEFT = 'hoe-left'
    HOE_RIGHT = 'hoe-right'
