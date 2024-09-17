from rest_framework import viewsets, status, permissions
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from orders.api.serializers import OrderSerializer, CreateOrderSerializer
from orders.core.services import OrderService
from orders.adapters.repository.django_orders import DjangoOrderRepository
from products.adapters.repository.django_products import DjangoProductRepository
from store_project.utils import handle_response, response_error_handler, body_validator
from orders.models import Order as DjangoOrderModel


class OrderViewSet(viewsets.ViewSet):
    """Handles the CRUD operations for the Order model"""

    repo = DjangoOrderRepository()
    product_repo = DjangoProductRepository()
    service = OrderService(repo, product_repo)
    queryset = DjangoOrderModel.objects.all()
    permission_classes = [permissions.AllowAny]

    # Get Method
    @swagger_auto_schema(
        operation_description="List all the orders",
        responses={200: OrderSerializer(many=True)},
    )
    def list(self, request):

        orders = self.service.list_orders()
        serializer = OrderSerializer(orders, many=True)
        return handle_response(serializer.data)

    # Get Method By ID
    @swagger_auto_schema(
        operation_description="Retrieve an order by id",
        responses={200: OrderSerializer},
        manual_parameters=[
            openapi.Parameter(
                "id",
                openapi.IN_PATH,
                description="Order Id",
                type=openapi.TYPE_INTEGER,
            )
        ],
    )
    def retrieve(self, request, pk=None):

        order = self.service.get_order(pk)
        if not order:
            return response_error_handler("Order not found", status.HTTP_404_NOT_FOUND)

        serializer = OrderSerializer(order)
        return handle_response(serializer.data)

    # Post Method
    @swagger_auto_schema(
        operation_description="Creates an order",
        request_body=CreateOrderSerializer,
        responses={201: OrderSerializer},
    )
    def create(self, request):

        order_data = request.data

        if not body_validator(order_data, ["items"]):
            return response_error_handler("Invalid body", status.HTTP_400_BAD_REQUEST)

        try:
            order = self.service.create_order(order_data["items"])
        except ValueError as e:
            return response_error_handler(str(e), status.HTTP_400_BAD_REQUEST)

        serializer = OrderSerializer(order)

        return handle_response(
            serializer.data, status.HTTP_201_CREATED, msg="Order created"
        )

    # Put Method
    @swagger_auto_schema(
        operation_description="Updates an order",
        request_body=CreateOrderSerializer,
        responses={200: OrderSerializer},
    )
    def update(self, request, pk=None):
        order_data = request.data

        # try:
        order = self.service.update_order(pk, order_data["items"])
        # except ValueError as e:
        #     return response_error_handler(str(e), status.HTTP_400_BAD_REQUEST)

        serializer = OrderSerializer(order)
        return handle_response(serializer.data, status.HTTP_200_OK, msg="Order updated")

    # Patch Method
    @swagger_auto_schema(
        operation_description="Updates an order",
        request_body=CreateOrderSerializer,
        responses={200: OrderSerializer},
    )
    def partial_update(self, request, pk=None):
        return self.update(request, pk)
