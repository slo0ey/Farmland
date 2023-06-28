from typing import *

Size = Tuple[int, int]
IntPosition = Tuple[int, int]
Position = Tuple[float, float]
Velocity = Tuple[float, float]

L = TypeVar('L')
LateInit = Union[L, None]


class StatusInfo:
    def __init__(
            self,
            alias: str,
            animate_speed: float = 1.0
    ):
        self.alias = alias
        self.animate_speed = animate_speed
