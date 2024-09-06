from django.db import models
from products.models import Product


class Order(models.Model):
    items = models.ManyToManyField(Product, through='OrderItem')
    base_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return f"Order {self.id}"
      


class OrderItem(models.Model):
    order = models.ForeignKey(
        Order, related_name='order_items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    class Meta:
        unique_together = ('order', 'product')

    def __str__(self):
        return f"{self.product.name} (x{self.quantity})"
