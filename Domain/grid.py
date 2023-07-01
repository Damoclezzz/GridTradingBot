class Grid:
    def __init__(self, price_line: float):
        self.price_line = price_line

    def __repr__(self):
        return f'Grid {self.price_line}'