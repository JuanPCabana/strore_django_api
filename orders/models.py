from django.db import models
from products.models import Product


class Order(models.Model):
    # items = models.ManyToManyField(OrderItem, through='OrderItem')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.id}"

    @property
    def order_base_price(self) -> float:
        """Returns the total base price of the order"""

        items: list[OrderItem] = self.items.all()
        return sum(item.total_base_price for item in items)

    @property
    def order_total_price(self) -> float:
        """Returns the total price of the order with tax"""

        items: list[OrderItem] = self.items.all()
        return sum(item.total_price for item in items)


class OrderItem(models.Model):

    order = models.ForeignKey(Order, related_name="items", on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.product.name} (x{self.quantity})"

    @property
    def total_base_price(self) -> float:
        """Returns the total base price of the item"""

        return self.product.base_price * self.quantity

    @property
    def total_item_price(self) -> float:
        """Returns the total price of the item"""

        return self.product.calculate_price_with_tax

    @property
    def total_price(self) -> float:
        """returns the total price of the item with tax"""

        return self.total_item_price * self.quantity

    @property
    def tax_fee_per_product(self) -> float:
        """Returns the tax fee per product"""

        return self.product.base_price * (self.product.tax_rate / 100)

    @property
    def total_tax_fee(self) -> float:
        """returns the sum of taxes corresponding to a product."""

        return self.tax_fee_per_product * self.quantity
