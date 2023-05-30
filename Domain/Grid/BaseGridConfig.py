from abc import ABC


class BaseGridConfig(ABC):
    def __init__(self, step: float):
        self.step = step
