from scene.base import BaseScene, BaseSceneContext
from world.farm import FarmWorld

from dataclasses import dataclass


@dataclass
class TestSceneContext(BaseSceneContext):
    pass


class TestScene(BaseScene):
    def __init__(
            self,
            context: TestSceneContext
    ):
        super().__init__(context)
        self.world = FarmWorld()

    def update(self, dt: float):
        self.world.update(dt)
