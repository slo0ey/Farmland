from reactivex.scheduler.mainloop import PyGameScheduler

from core.rx import Rx
from event.base import FrameEvent, KeyDownEvent, KeyUpEvent
from scene.test import TestScene, TestSceneContext
from util.types import Size

import sys
import pygame


class Game:
    def __init__(self, title: str, size: Size = (1600, 900)):
        # General setup
        pygame.init()
        pygame.display.set_caption(title)
        self.screen = pygame.display.set_mode(size)
        self.clock = pygame.time.Clock()

        # Rx setup
        Rx.set_scheduler(PyGameScheduler(pygame))

        # Test setup
        self.scene = TestScene(
            context=TestSceneContext()
        )

    def run(self):
        is_running = True
        while is_running:
            dt = self.clock.tick(60) / 1000

            Rx.frame.on_next(FrameEvent(dt))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    is_running = False
                elif event.type == pygame.KEYDOWN:
                    Rx.keydown.on_next(KeyDownEvent(
                        dt=dt,
                        keys=pygame.key.get_pressed()
                    ))
                elif event.type == pygame.KEYUP:
                    Rx.keyup.on_next(KeyUpEvent(
                        dt=dt,
                        keys=pygame.key.get_pressed()
                    ))
            self.scene.update(dt)
            pygame.display.update()

        pygame.quit()
        sys.exit()
