from uuid import uuid4
from datetime import datetime


class Product:
    def __init__(self, sku, name, price, quantity=0, description="", uuid=None, created_at=None, **kwargs):
        self.sku = sku
        self.name = name
        self.price = price
        self.quantity = quantity
        self.description = description
        self.uuid = str(uuid) if uuid else str(uuid4())
        self.created_at = created_at if created_at else datetime.now()

    def to_dict(self):
        return {
            "sku": self.sku,
            "name": self.name,
            "price": self.price,
            "quantity": self.quantity,
            "description": self.description,
            "uuid": self.uuid,
            "created_at": self.created_at,
        }
