from abc import ABC, abstractmethod
from products.core.models import Product


class ProductRepository(ABC):
    @abstractmethod
    def save(self, product: Product) -> Product:
        """Saves a product in the database of Django

        Args:
            product: Product object

        Returns:
            Product: Returns the product saved in the database
        """
        pass

    @abstractmethod
    def update(self, product: Product) -> Product:
        """Updates a product in the database of Django

        Args:
            product: Product object

        Returns:
            Product: returns the updated product

        """
        pass

    @abstractmethod
    def get_by_id(self, product_id: int) -> Product:
        """Retuns a product from the database of Django

        Args:
            product_id: product id

        Returns:
            Product: Product object.

        """
        pass

    @abstractmethod
    def list_all(self) -> list[Product]:
        """Retrieves all products from the database of Django

        Returns:
            Product: Product object
        """
        pass
