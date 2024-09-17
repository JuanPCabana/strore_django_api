from rest_framework import serializers

# from .models import Product
from products.models import Product as DjangoProductModel


# Serializers for the models
class ProductSerializer(serializers.ModelSerializer):
    """Serializer for the Product model"""

    class Meta:
        model = DjangoProductModel
        ref_name = "Product_data"
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


# Serializers for the requests


class CreateProductSerializer(serializers.Serializer):
    """Serializer for the Create Product model"""

    reference = serializers.CharField(max_length=50, help_text="Product reference")
    name = serializers.CharField(max_length=100, help_text="Product name")
    description = serializers.CharField(max_length=255, help_text="Product description")
    base_price = serializers.DecimalField(
        max_digits=10, decimal_places=2, help_text="Product base price"
    )
    tax_rate = serializers.DecimalField(
        max_digits=10,
        decimal_places=2,
        help_text="Product tax rate on percentage withouth the % symbol",
    )

    class Meta:
        fields = (
            "reference",
            "name",
            "description",
            "base_price",
            "tax_rate",
        )


class UpdateProductSerializer(serializers.Serializer):
    """Serializer for the Update Product model"""

    reference = serializers.CharField(
        max_length=50, help_text="Product reference", required=False
    )
    name = serializers.CharField(
        max_length=100, help_text="Product name", required=False
    )
    description = serializers.CharField(
        max_length=255, help_text="Product description", required=False
    )
    base_price = serializers.DecimalField(
        max_digits=10, decimal_places=2, help_text="Product base price", required=False
    )
    tax_rate = serializers.DecimalField(
        max_digits=10,
        decimal_places=2,
        help_text="Product tax rate on percentage withouth the % symbol",
        required=False,
    )

    class Meta:
        fields = (
            "reference",
            "name",
            "description",
            "base_price",
            "tax_rate",
        )
