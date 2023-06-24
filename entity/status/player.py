from enum import Enum


class PlayerStatus(Enum):
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

    def is_on_move(self):
        return self.value.split('-')[0] in ('idle', 'walk')

    def is_on_tool(self):
        return self.value.split('-')[0] in ('hoe', 'plant', 'watering', 'harvest', 'axe')
