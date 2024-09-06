from orders.ports.repositories import OrderRepository
from orders.core.models import Order
from orders.models import Order as DjangoOrderModel
from products.models import Product as DjangoProductModel


class DjangoOrderRepository(OrderRepository):
    def save(self, order: Order):
        django_order = DjangoOrderModel.objects.create(
            created_at=order.created_at
        )
        base_price = 0
        total_price = 0
        for product_id, quantity in order.items:
            product_data = DjangoProductModel.objects.get(id=product_id)
            base_price += product_data.base_price * quantity
            total_price += product_data.calculate_price_with_tax() * quantity
            django_order.items.create(product_id=product_id, quantity=quantity)
        
        django_order.base_price = base_price
        django_order.total_price = total_price
        django_order.save()
        
        order.id = django_order.pk
        return order

    def update(self, order):
        django_order = DjangoOrderModel.objects.get(id=order.id)
        django_order.items.clear()
        for article, quantity in order.items:
            django_order.items.create(article_id=article.id, quantity=quantity)
        django_order.save()
        return order

    def get_by_id(self, order_id):
        django_order = DjangoOrderModel.objects.get(id=order_id)
        items = [
            (Article(
                reference=item.article.reference,
                name=item.article.name,
                description=item.article.description,
                price=item.article.price,
                tax_rate=item.article.tax_rate
            ), item.quantity)
            for item in django_order.items.all()
        ]
        return Order(items)

    def list_all(self):
        return [self.get_by_id(order.id) for order in DjangoOrderModel.objects.all()]
