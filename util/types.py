from enum import Enum
from typing import *


Size = Tuple[int, int]
Position = Tuple[float, float]
Velocity = Tuple[float, float]


class Status(str, Enum):
    def _generate_next_value_(name: str, start: int, count: int, last_values: list[Any]) -> Any:
        return name

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name
