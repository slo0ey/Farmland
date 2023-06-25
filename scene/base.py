from dataclasses import dataclass
from typing import TypeVar


@dataclass
class BaseSceneContext:
    pass


C = TypeVar('C', bound=BaseSceneContext)


class BaseScene:
    def __init__(
            self,
            context: C | None = None
    ):
        self.context = context

    def update(self, dt: float):
        pass
