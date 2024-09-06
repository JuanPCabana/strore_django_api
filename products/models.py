from django.db import models


class Product(models.Model):
    reference = models.CharField(max_length=50)
    name = models.CharField(max_length=255)
    description = models.TextField()
    base_price = models.DecimalField(max_digits=6, decimal_places=2)
    tax_rate = models.DecimalField(max_digits=4, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    @property
    def calculate_price_with_tax(self):
        return self.base_price + ((self.tax_rate / 100) * self.base_price)
