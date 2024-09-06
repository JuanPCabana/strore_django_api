from abc import ABC, abstractmethod
from products.core.models import Product


class ProductRepository(ABC):
    @abstractmethod
    def save(self, product: Product) -> Product:
        """Guarda un producto en la base de datos de Django

        Args:
            product: Objeto de tipo Product

        Returns:
            Product: Retorna el producto creado con el id asignado
        """
        pass

    @abstractmethod
    def update(self, product: Product) -> Product:
        """Actualiza un producto en la base de datos de Django

        Args:
            product: Objeto de tipo Product

        Returns:
            Product: Retorna el producto actualizado con el id asignado
            
        """
        pass

    @abstractmethod
    def get_by_id(self, product_id: int) -> Product:
        """Retorna un producto en la base de datos de Django

        Args:
            product_id: id del producto (Int)

        Returns:
            Product: Retorna el producto correspondiente al id
            
        Puede ser None si no se encuentra el producto
        """
        pass

    @abstractmethod
    def list_all(self)-> list[Product]:
        """Retorna todos los productos en la base de datos de Django

        Returns:
            Product: Retorna una lista de productos
        """
        pass
