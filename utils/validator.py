from db import product_data

def validate_product_data(data):
    error = {}

    if not data.get("sku"):
        error["sku"] = "SKU is required"

    if not data.get("name"):
        error["name"] = "Name is required"

    if not data.get("price"):
        error["price"] = "Price is required"

    if data.get("sku") and not isinstance(data.get("sku"), str):
        error["sku"] = "SKU should be a string"

    if data.get("name") and not isinstance(data.get("name"), str):
        error["name"] = "Name should be a string"

    if data.get("price") and not isinstance(data.get("price"), (int, float)):
        error["name"] = "price should be a number"


    if data.get("sku") and isinstance(data.get("sku"), str) and not data.get("sku").startswith("P_"):
        error["sku_pattern"] = f"SKU {data.get("sku")} should start with P_."

    for product in product_data:
        if product.sku == data.get("sku"):
            error["sku"] = f"SKU {data.get("sku")} already exists."
            
    return error        
