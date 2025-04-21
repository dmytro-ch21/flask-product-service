from models.product_model import Product

product1 = Product(
    sku="P_001",
    name="iPhone 16 Pro",
    price=999.99,
    quantity=100,
    description="Nice smartphone"
)

product2 = Product(
    sku="P_002",
    name="Dell Laptop XP500",
    price=1299.99,
    quantity=10,
    description="A high-performance laptop - Intel i7 - Nvidia GTX 5080 - 32GB"
)

product_data = [product1, product2]
