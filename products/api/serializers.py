from rest_framework import serializers

# from .models import Product
from products.models import Product as DjangoProductModel


class ProductSerializer(serializers.ModelSerializer):
    """Serializer for the Product model"""

    class Meta:
        model = DjangoProductModel
        fields = (
            "id",
            "reference",
            "name",
            "description",
            "base_price",
            "tax_rate",
            "created_at",
            "updated_at",
        )
        read_only_fields = ("created_at",)


class ShortProductSerializer(serializers.ModelSerializer):
    """Serializer for the Product model with less fields"""

    class Meta:
        model = DjangoProductModel
        fields = (
            "id",
            "reference",
            "name",
            "base_price",
            "tax_rate",
        )
        read_only_fields = ("created_at",)
