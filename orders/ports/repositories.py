from abc import ABC, abstractmethod
from orders.core.models import Order


class OrderRepository(ABC):
    @abstractmethod
    def save(self, order: Order):
        pass

    @abstractmethod
    def update(self, order: Order):
        pass

    @abstractmethod
    def get_by_id(self, order_id):
        pass

    @abstractmethod
    def list_all(self):
        pass
