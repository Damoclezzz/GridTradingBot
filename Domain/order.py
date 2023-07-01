from typing import List
from grid import Grid


class Order:
    def __init__(self, enter_price: float, exit_price: float):
        self.enter_price = enter_price
        self.exit_price = exit_price

        self.grids: List[Grid] = []

    def __repr__(self):
        return f'Order: enter price - {self.enter_price}, exit price - {self.exit_price}'

    def set_grids(self, grid_step: float):
        self.grids = []
        pointer = self.enter_price

        while pointer <= self.exit_price:
            self.grids.append(Grid(pointer))
            pointer += grid_step


class OrderFactory:
    @staticmethod
    def create_orders(
            create_orders_up: int,
            create_orders_down: int,
            width: float,
            step: float,
            rate: float
    ) -> List[Order]:
        # TODO: Можно добавить обработку ошибок если count <= 0
        orders_list = [OrderFactory.__create_central_order(rate, width)]

        for i in range(create_orders_up):
            central_order = orders_list[-1]
            orders_list.append(OrderFactory.__create_up_order(central_order, step, width))

        for i in range(create_orders_down):
            central_order = orders_list[0]
            orders_list.insert(0, OrderFactory.__create_down_order(central_order, step, width))

        return orders_list

    @staticmethod
    def __create_central_order(rate: float, width: float) -> Order:
        enter_price = rate - width / 2
        exit_price = rate + width / 2

        return Order(enter_price, exit_price)

    @staticmethod
    def __create_up_order(central_order: Order, step: float, width: float) -> Order:
        enter_price = central_order.exit_price - step
        exit_price = enter_price + width

        return Order(enter_price, exit_price)

    @staticmethod
    def __create_down_order(central_order: Order, step: float, width: float) -> Order:
        exit_price = central_order.enter_price + step
        enter_price = exit_price - width

        return Order(enter_price, exit_price)


if __name__ == '__main__':
    orders = OrderFactory.create_orders(create_orders_up=2, create_orders_down=1, width=500, step=450, rate=30150)
    for order in orders:
        print(order)
    # for order in OrderFactory.create_orders(create_orders_count=3, width=60, step=30, rate=27100):
    #     order.set_grids(10)
    #     print(order)
