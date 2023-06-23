from dataclasses import dataclass


@dataclass
class FrameEvent:
    dt: float

    def unpack(self):
        return tuple([self.dt])
