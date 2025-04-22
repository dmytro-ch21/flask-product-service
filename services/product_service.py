from db import product_data
from models.product_model import Product
from utils.validator import validate_product_data
from repositories.product_repository import ProductRepository

class ProductService:
    @staticmethod
    def get_all_products():
        products = ProductRepository.get_all_products() # list of dictionaries [dict, dict]
        if not products:
            return []
        return [Product(**p) for p in products]
    
    @staticmethod
    def get_product_by_sku(sku: str):
        product = ProductRepository.get_product_by_sku(sku)
        return Product(**product) if product else None
    
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
        
        creted_product = ProductRepository.create_product(new_product)
        products = ProductRepository.get_all_products()
        return [Product(**p) for p in products]
         
    @staticmethod
    def delete_product(sku):
        deleted  = ProductRepository.delete_product(sku)
        products = ProductRepository.get_all_products()
        return True, [Product(**p) for p in products]