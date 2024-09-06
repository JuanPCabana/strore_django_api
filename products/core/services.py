from decimal import Decimal

from .models import Product
from products.ports.repositories import ProductRepository


class ProductService:
    def __init__(self, product_repository: ProductRepository):
        self.product_repository = product_repository

    def create_product(
        self,
        reference: str,
        name: str,
        description: str,
        base_price: float,
        tax_rate: float,
    ) -> Product:
        """Saves a product in the database

        Args:
            reference (str): product reference
            name (str): product name
            description (str): product description
            base_price (float): product base price
            tax_rate (float): product tax rate

        Returns:
            Product: Returns the product saved in the database
        """
        product = Product(reference, name, description, base_price, tax_rate)
        self.product_repository.save(product)
        return product

    def update_product(self, product_id: int, **kwargs) -> Product:
        """Updates a product in the database

        Args:
            product_id (int): product id
            **kwargs: fields to update

        Returns:
            Product: returns the updated product
        """

        product = self.product_repository.get_by_id(product_id)
        if not product:
            return None
        for key, value in kwargs.items():
            if value is not None:
                setattr(product, key, value)
        product.tax_rate = Decimal(product.tax_rate)
        product.base_price = Decimal(product.base_price)
        self.product_repository.update(product)
        return product

    def get_product(self, product_id: int) -> Product:
        """Retorna un producto en la base de datos de Django

        Args:
            product_id: id del producto (Int)

        Returns:
            Product: Retorna el producto correspondiente al id
        """
        return self.product_repository.get_by_id(product_id)

    def list_products(self) -> list[Product]:
        """Retorna todos los productos en la base de datos de Django

        Returns:
            Product: Retorna una lista de productos
        """
        return self.product_repository.list_all()
