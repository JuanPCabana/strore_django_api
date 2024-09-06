from .models import Order, OrderItem
from orders.ports.repositories import OrderRepository
from products.ports.repositories import ProductRepository


class OrderService:
    def __init__(
        self, order_repository: OrderRepository, product_repository: ProductRepository
    ):
        self.order_repository = order_repository
        self.product_repository = product_repository

    def create_order(self, items_data: list) -> Order:

        items = []

        for item_data in items_data:
            product = self.product_repository.get_by_id(item_data["product_id"])
            items.append((product, item_data["quantity"]))

        order = Order(items=items)
        self.order_repository.save(order)
        order.items = [
            OrderItem(product=item[0], quantity=item[1], order=order) for item in items
        ]
        return order

    def update_order(self, order_id: int, items_data: list[dict]) -> Order:
        items = []

        for item_data in items_data:
            product = self.product_repository.get_by_id(item_data["product_id"])
            items.append((product, item_data["quantity"]))

        new_order = Order(items=items)
        new_order.id = order_id

        return self.order_repository.update(new_order)

    def get_order(self, order_id: int) -> Order:
        return self.order_repository.get_by_id(order_id)

    def list_orders(self) -> list[Order]:
        return self.order_repository.list_all()
