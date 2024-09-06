from django.contrib import admin
from orders.models import Order, OrderItem


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("id", "created_at", "order_base_price", "order_total_price")
    readonly_fields = ("order_base_price", "order_total_price")
    search_fields = ("id",)
    list_filter = ("created_at",)


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = (
        "product",
        "quantity",
        "total_base_price",
        "total_item_price",
        "total_price",
        "tax_fee_per_product",
        "order",
    )
    search_fields = ("product__name", "order__id")
    readonly_fields = (
        "total_base_price",
        "total_item_price",
        "total_price",
        "tax_fee_per_product",
    )
    list_filter = ("product", "order")
