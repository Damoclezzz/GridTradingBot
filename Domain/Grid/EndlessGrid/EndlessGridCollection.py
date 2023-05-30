from typing import Dict

from Domain.Grid.Grid import Grid
from Domain.Grid.EndlessGrid import EndlessGridConfig


class EndlessGridCollection:
    MAX_VALUE = 100000

    def __init__(self, grid_config: EndlessGridConfig):
        self.grids: Dict[int, Grid] = {}

        for price in range(0 + grid_config.step, EndlessGridCollection.MAX_VALUE, grid_config.step):
            self.grids[price] = Grid(price)
