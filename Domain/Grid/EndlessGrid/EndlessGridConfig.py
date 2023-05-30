from ..BaseGridConfig import BaseGridConfig


class EndlessGridConfig(BaseGridConfig):
    def __init__(self, step: float):
        super().__init__(step)
