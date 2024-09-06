from orders.ports.repositories import OrderRepository
from orders.core.models import Order
from orders.models import Order as DjangoOrderModel
from products.models import Product as DjangoProductModel


class DjangoOrderRepository(OrderRepository):
    """
    Handles the persistence of products in the Django database.

    The methods save, update, get_by_id, and list_all are implemented.

    These methods are documented in the OrderRespository interface.

    """

    def save(self, order: Order) -> Order:
        django_order = DjangoOrderModel.objects.create(created_at=order.created_at)

        for product_data, quantity in order.items:
            django_order.items.create(product=product_data, quantity=quantity)

        order.id = django_order.pk

        return order

    def update(self, order: Order) -> Order:
        django_order = DjangoOrderModel.objects.get(id=order.id)
        django_order.items.all().delete()

        for product, quantity in order.items:
            try:
                product_data = DjangoProductModel.objects.get(id=product.id)
            except DjangoProductModel.DoesNotExist:
                raise ValueError(f"Product with id {product.id} does not exist")

            django_order.items.create(product=product_data, quantity=quantity)

        django_order.save()
        django_order.refresh_from_db()
        return django_order

    def get_by_id(self, order_id: int) -> Order:

        try:
            django_order = DjangoOrderModel.objects.get(id=order_id)
        except DjangoOrderModel.DoesNotExist:
            raise ValueError(f"Order with id {order_id} does not exist")

        return django_order

    def list_all(self) -> list[Order]:
        elements = [
            self.get_by_id(order.id) for order in DjangoOrderModel.objects.all()
        ]

        return elements
