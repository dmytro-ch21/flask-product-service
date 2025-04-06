from db import product_data
from models.product_model import Product
from utils.validator import validate_product_data

class ProductService:
    @staticmethod
    def get_all_products():
        return product_data
    
    @staticmethod
    def get_product_by_sku(sku: str):
        for product in product_data:
            if product.sku == sku:
                return product
        return None
    
    @staticmethod
    def create_product(data: dict):
        # validate if the data is complete and has the required fields
        error = validate_product_data(data)
        
        if error:
            return error
            
        # create new product
        new_product = Product(
            sku=data.get("sku"),
            name=data.get("name"),
            price=data.get("price"),
            quantity=data.get("quantity", 1),
            description=data.get("description", "")
        )
        
        # append the new product to the data source
        product_data.append(new_product)
        return product_data
         
    @staticmethod
    def delete_product(sku):
        for product in product_data:
            if product.sku == sku:
                product_data.remove(product)
                return True, product_data
        return False, None           