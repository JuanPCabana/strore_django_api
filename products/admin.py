from django.contrib import admin
from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('reference', 'name', 'base_price',
                    'tax_rate', 'created_at')
    search_fields = ('reference', 'name')
    list_filter = ('created_at',)
