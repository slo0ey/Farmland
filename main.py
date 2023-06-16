import sys
import pygame

from world import FarmWorld


class Game:
    def __init__(self, title: str, size: tuple[float, float] = (1600, 900)):
        pygame.init()
        pygame.display.set_caption(title)
        self.screen = pygame.display.set_mode(size)
        self.clock = pygame.time.Clock()
        self.world = FarmWorld()

    def run(self):
        is_running = True
        while is_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    is_running = False

            delta_time = self.clock.tick(60) / 1000
            self.world.run(delta_time)
            pygame.display.update()

        pygame.quit()
        sys.exit()


if __name__ == "__main__":
    game = Game("Farmland!", size=(1600, 900))
    game.run()
