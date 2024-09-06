from datetime import datetime
from products.core.models import Product


class OrderItem:
    def __init__(self, product: Product, quantity: int, order: int):
        self.product = product
        self.quantity = quantity
        self.order = order

    # def calculate_base_total(self):
    #     return self.product.base_price * self.quantity

    # def calculate_total_price(self):
    #     itemTax = self.product.base_price * (self.product.tax_rate/100)
    #     return (self.product.base_price + itemTax) * self.quantity


class Order:
    def __init__(self, items: list[tuple[int, int]]):
        self.id = None  # Se asigna al guardar
        self.items = items
        self.created_at = datetime.now()
        # self.base_price = sum([item.calculate_base_total() for item in items])
        # self.total_price = sum([item.calculate_total_price() for item in items])
