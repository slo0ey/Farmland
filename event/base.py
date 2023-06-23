from dataclasses import dataclass

import pygame


@dataclass
class FrameEvent:
    dt: float

    def unpack(self):
        return tuple([self.dt])


@dataclass
class KeyDownEvent(FrameEvent):
    keys: pygame.key.ScancodeWrapper

    def unpack(self):
        return self.dt, self.keys


@dataclass
class KeyUpEvent(FrameEvent):
    keys: pygame.key.ScancodeWrapper

    def unpack(self):
        return self.dt, self.keys


@dataclass
class MouseDownEvent(FrameEvent):
    def unpack(self):
        return tuple([self.dt])


@dataclass
class MouseUpEvent(FrameEvent):
    def unpack(self):
        return tuple([self.dt])
