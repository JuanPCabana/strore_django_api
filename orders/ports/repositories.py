from abc import ABC, abstractmethod
from orders.core.models import Order


class OrderRepository(ABC):
    @abstractmethod
    def save(self, order: Order) -> Order:
        """Saves an order in the database.

        Args:
            order (Order): Order Object to be saved in the database.

         Returns:
            Order: Order object Saved from the database.
        """
        pass

    @abstractmethod
    def update(self, order: Order) -> Order:
        """Updates an order in the database.

        Args:
            order (Order): Order Object to be updated in the database.

        Returns:
            Order: Order object Updated from the database.
        """
        pass

    @abstractmethod
    def get_by_id(self, order_id) -> Order:
        """Gets an order by its id.

        Args:
            order_id (int): Order id to be retrieved.

        Returns:
            Order: Order object retrieved from the database.
        """
        pass

    @abstractmethod
    def list_all(self):
        """Retieves all orders from the database."""
        pass
