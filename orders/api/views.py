from rest_framework import viewsets, status, permissions
from rest_framework.response import Response
from orders.api.serializers import OrderSerializer
from orders.core.services import OrderService
from orders.adapters.repository.django_orders import DjangoOrderRepository
from products.adapters.repository.django_products import DjangoProductRepository


class OrderViewSet(viewsets.ViewSet):
    repo = DjangoOrderRepository()
    product_repo = DjangoProductRepository()
    service = OrderService(repo, product_repo)
    queryset = service.list_orders()
    permission_classes = [permissions.AllowAny]

    def list(self, request):

        orders = self.service.list_orders()
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):

        order = self.service.get_order(pk)
        if order:
            serializer = OrderSerializer(order)
            return Response(serializer.data)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def create(self, request):
        order_data = request.data
        order = self.service.create_order(order_data['items'])
        serializer = OrderSerializer(order)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk=None):
        order_data = request.data
        order = self.service.update_order(pk, order_data['items'])
        serializer = OrderSerializer(order)
        return Response(serializer.data, status=status.HTTP_200_OK)
