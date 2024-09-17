from rest_framework import serializers
from orders.models import Order as DjangoOrderModel, OrderItem as DjangoOrderItemModel
from products.models import Product as DjangoProductModel

# Serializers for the models
class ProductSerializer(serializers.ModelSerializer):
    """Serializer for the Product model"""

    class Meta:
        model = DjangoProductModel
        fields = ["id", "name", "base_price", "tax_rate", "reference"]


class OrderItemSerializer(serializers.ModelSerializer):
    """Serializer for the OrderItem model"""

    product = ProductSerializer()
    total_base_price = serializers.ReadOnlyField()
    total_item_price = serializers.ReadOnlyField()
    total_price = serializers.ReadOnlyField()
    tax_fee_per_product = serializers.ReadOnlyField()
    total_tax_fee = serializers.ReadOnlyField()

    class Meta:
        model = DjangoOrderItemModel
        fields = [
            "product",
            "quantity",
            "total_base_price",
            "total_item_price",
            "total_price",
            "tax_fee_per_product",
            "total_tax_fee",
        ]


class OrderSerializer(serializers.ModelSerializer):
    """Serializer for the Order model"""

    items = OrderItemSerializer(many=True, read_only=True)
    order_base_price = serializers.ReadOnlyField()
    order_total_price = serializers.ReadOnlyField()

    class Meta:
        model = DjangoOrderModel
        fields = ["id", "created_at", "items", "order_base_price", "order_total_price"]


# Serializers for the requests

class CreateOrderSerializer(serializers.Serializer):
    """Serializer for the Create Order model"""

    class ItemSerializer(serializers.Serializer):
        product_id = serializers.IntegerField(help_text="Product ID")
        quantity = serializers.IntegerField(
            help_text="Product quantity to add to the order"
        )

        class Meta:
            fields = ["product_id", "quantity"]

    items = serializers.ListField(
        child=ItemSerializer(),
        allow_empty=False,
    )
