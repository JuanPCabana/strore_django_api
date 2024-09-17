from rest_framework import viewsets, status, permissions
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from products.api.serializers import (
    ProductSerializer,
    ShortProductSerializer,
    CreateProductSerializer,
    UpdateProductSerializer,
)
from products.adapters.repository.django_products import DjangoProductRepository
from products.core.services import ProductService
from store_project.utils import response_error_handler, body_validator, handle_response
from products.models import Product as DjangoProductModel


class ProductViewSet(viewsets.ViewSet):
    repo = DjangoProductRepository()
    service = ProductService(repo)
    queryset = DjangoProductModel.objects.all()
    permission_classes = [permissions.AllowAny]
    productSerializer = ProductSerializer
    shortProductSerializer = ShortProductSerializer

    # Get Method
    @swagger_auto_schema(
        operation_description="Lists all the products",
        responses={200: ShortProductSerializer(many=True)},
    )
    def list(self, request):

        products = self.service.list_products()
        serializer = self.shortProductSerializer(products, many=True)

        return handle_response(serializer.data)

    # Get Method By ID
    @swagger_auto_schema(
        operation_description="Retrieve a product by id",
        responses={200: ProductSerializer},
        manual_parameters=[
            openapi.Parameter(
                "id",
                openapi.IN_PATH,
                description="Product Id",
                type=openapi.TYPE_INTEGER,
            )
        ],
    )
    def retrieve(self, request, pk=None):
        """Retrieves a product"""

        product = self.service.get_product(pk)
        if not product:
            return response_error_handler(
                "Producto no encontrado", status.HTTP_404_NOT_FOUND
            )

        serializer = self.productSerializer(product)

        return handle_response(serializer.data)

    # Post Method
    @swagger_auto_schema(
        operation_description="Creates a product",
        request_body=CreateProductSerializer,
        responses={201: ProductSerializer},
    )
    def create(self, request):
        """Creates a product"""

        product_data: dict = request.data

        valid = body_validator(
            data=product_data,
            required_fields=[
                "reference",
                "name",
                "description",
                "base_price",
                "tax_rate",
            ],
        )
        if not valid:
            return response_error_handler(
                "Faltan campos requeridos", status.HTTP_400_BAD_REQUEST
            )

        try:
            product = self.service.create_product(
                reference=product_data["reference"],
                name=product_data["name"],
                description=product_data["description"],
                base_price=product_data["base_price"],
                tax_rate=product_data["tax_rate"],
            )
        except ValueError as e:
            return response_error_handler("Bad Request", status.HTTP_400_BAD_REQUEST)

        serializer = self.productSerializer(product)

        return handle_response(serializer.data, status_code=status.HTTP_201_CREATED)

    # Put Method
    @swagger_auto_schema(
        operation_description="Updates a product",
        request_body=UpdateProductSerializer,
        responses={200: ProductSerializer},
    )
    def update(self, request, pk=None):
        """Updates a product"""

        product_data: dict = request.data

        valid = body_validator(data=product_data)
        if not valid:
            return response_error_handler(
                "Faltan campos requeridos", status.HTTP_400_BAD_REQUEST
            )

        try:
            product = self.service.update_product(
                pk,
                reference=product_data.get("reference"),
                name=product_data.get("name"),
                description=product_data.get("description"),
                base_price=product_data.get("base_price"),
                tax_rate=product_data.get("tax_rate"),
            )
        except ValueError as e:
            return response_error_handler("Bad Request", status.HTTP_400_BAD_REQUEST)

        if not product:
            return response_error_handler(
                "Producto no encontrado", status.HTTP_404_NOT_FOUND
            )

        serializer = self.productSerializer(product)

        return handle_response(serializer.data, status_code=status.HTTP_200_OK)

    # Patch Method
    @swagger_auto_schema(
        operation_description="Updates a product",
        request_body=UpdateProductSerializer,
        responses={200: ProductSerializer},
    )
    def partial_update(self, request, *args, **kwargs):
        """Partial update of a product"""

        return self.update(request, *args, **kwargs)
