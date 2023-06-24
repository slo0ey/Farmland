from util.types import StatusInfo

from enum import Enum


class PlayerStatus(Enum):
    STAND = StatusInfo('stand')
    WALK_UP = StatusInfo('walk-up')
    WALK_DOWN = StatusInfo('walk-down')
    WALK_LEFT = StatusInfo('walk-left')
    WALK_RIGHT = StatusInfo('walk-right')
    IDLE_UP = StatusInfo('idle-up')
    IDLE_DOWN = StatusInfo('idle-down')
    IDLE_LEFT = StatusInfo('idle-left')
    IDLE_RIGHT = StatusInfo('idle-right')
    HOE_UP = StatusInfo('hoe-up', 4)
    HOE_DOWN = StatusInfo('hoe-down', 4)
    HOE_LEFT = StatusInfo('hoe-left', 4)
    HOE_RIGHT = StatusInfo('hoe-right', 4)

    def is_on_move(self):
        return self.name.split('_')[0] in ('IDLE', 'WALK')

    def is_on_tool(self):
        return self.name.split('_')[0] in ('HOE', 'PLANT', 'WATERING', 'HARVEST', 'AXE')
