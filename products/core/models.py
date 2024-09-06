from datetime import datetime


class Product:
    def __init__(self, reference: str, name: str, description: str, base_price: float, tax_rate: float) -> None:
        self.id = None
        self.reference = reference
        self.name = name
        self.description = description
        self.base_price = float(base_price)
        self.tax_rate = float(tax_rate)
        self.created_at = datetime.now()

    def calculate_price_with_tax(self) -> float:
        return self.base_price + ((self.tax_rate/100) * self.base_price)
