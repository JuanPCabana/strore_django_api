from .models import Order, OrderItem
from orders.ports.repositories import OrderRepository
from products.ports.repositories import ProductRepository


class OrderService:
    def __init__(self, order_repository: OrderRepository, product_repository: ProductRepository):
        self.order_repository = order_repository
        self.product_repository = product_repository

    def create_order(self, items_data: list):
        items = []
        for item in items_data:
            item_id = item['product_id']
            quantity = item['quantity']
            items.append((item_id, quantity))

        order = Order(items=items)
        self.order_repository.save(order)
        return order

    def update_order(self, order_id, items_data):
        order = self.order_repository.get_by_id(order_id)
        items = []
        for item_data in items_data:
            article = self.product_repository.get_by_id(
                item_data['article_id'])
            items.append((article, item_data['quantity']))
        order.items = items
        self.order_repository.update(order)
        return order

    def get_order(self, order_id):
        return self.order_repository.get_by_id(order_id)

    def list_orders(self):
        return self.order_repository.list_all()
