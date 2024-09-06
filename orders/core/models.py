from datetime import datetime
from products.core.models import Product


class Order:
    def __init__(self, items: list[tuple[Product, int]]):
        self.id = None
        self.items = items
        self.created_at = datetime.now()

    @property
    def order_base_price(self):
        """Returns the total base price of the order"""

        items: list[OrderItem] = self.items.all()
        return sum(item.total_base_price for item in items)

    @property
    def order_total_price(self):
        """Returns the total price of the order with tax"""

        items: list[OrderItem] = self.items.all()
        return sum(item.total_price for item in items)


class OrderItem:
    def __init__(self, product: Product, quantity: int, order: Order):
        self.order = order
        self.product = product
        self.quantity = quantity

    @property
    def total_base_price(self):
        """Returns the total base price of the item"""

        return self.product.base_price * self.quantity

    @property
    def total_item_price(self):
        """Returns the total price of the item"""

        return self.product.calculate_price_with_tax

    @property
    def total_price(self):
        """returns the total price of the item with tax"""

        return self.total_item_price * self.quantity

    @property
    def tax_fee_per_product(self):
        """Returns the tax fee per product"""

        return self.product.base_price * (self.product.tax_rate / 100)

    @property
    def total_tax_fee(self):
        """returns the sum of taxes corresponding to a product."""

        return self.tax_fee_per_product * self.quantity
