from products.ports.repositories import ProductRepository
from products.core.models import Product
from products.models import Product as DjangoProductModel


class DjangoProductRepository(ProductRepository):
    """
    Handles the persistence of products in the Django database.

    The methods save, update, get_by_id, and list_all are implemented.

    These methods are documented in the ProductRepository interface.

    """

    def save(self, product: Product) -> Product:
        django_product = DjangoProductModel.objects.create(
            reference=product.reference,
            name=product.name,
            description=product.description,
            base_price=product.base_price,
            tax_rate=product.tax_rate,
            created_at=product.created_at,
        )

        product.id = django_product.pk

        return product

    def update(self, product: Product) -> Product:
        # django_product = DjangoProductModel.objects.get(id=product.id)
        django_product = self.get_by_id(product.id)

        if not django_product:
            return None

        django_product.reference = product.reference
        django_product.name = product.name
        django_product.description = product.description
        django_product.base_price = product.base_price
        django_product.tax_rate = product.tax_rate
        try:
            django_product.save()
        except ValueError as e:
            print(e)
            return None

        return product

    def get_by_id(self, product_id: int) -> Product:
        try:
            django_product = DjangoProductModel.objects.get(id=product_id)
        except DjangoProductModel.DoesNotExist:
            return None

        return django_product

    def list_all(self) -> list[Product]:
        return [a for a in DjangoProductModel.objects.all()]
