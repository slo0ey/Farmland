from enum import Enum
from typing import *


class Status(str, Enum):
    def _generate_next_value_(name: str, start: int, count: int, last_values: list[Any]) -> Any:
        return name

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name


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
