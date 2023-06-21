from reactivex.scheduler.mainloop import PyGameScheduler
from reactivex.subject import Subject

from util.types import Size
from world.farm import FarmWorld

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
        self.scheduler = PyGameScheduler(pygame)
        self.keydown = Subject()
        self.keyup = Subject()

        # Test setup
        self.world = FarmWorld()

    def run(self):
        is_running = True
        while is_running:
            dt = self.clock.tick(60) / 1000

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    is_running = False
                elif event.type == pygame.KEYDOWN:
                    self.keydown.on_next(dt)
                elif event.type == pygame.KEYUP:
                    self.keyup.on_next(dt)

            self.world.run(dt)
            pygame.display.update()

        pygame.quit()
        sys.exit()


GAME: Game | None = None

if __name__ == "__main__":
    GAME = Game("Farmland!", size=(1600, 900))
    GAME.run()
