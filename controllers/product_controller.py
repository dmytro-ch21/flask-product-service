from flask import Blueprint, jsonify, request
from services.product_service import ProductService

product_bp = Blueprint("products", __name__, url_prefix="/api/v2")

@product_bp.route("/products", methods=["GET"])
def get_products():
    products = ProductService.get_all_products()
    return jsonify([product.to_dict() for product in products])

@product_bp.route("/products/<string:sku>", methods=["GET"])
def get_product(sku):
    product = ProductService.get_product_by_sku(sku)
    if product:
        return jsonify(product.to_dict())
    return jsonify({"error": "Product not found"}), 404

@product_bp.route("/products", methods=["POST"])
def add_product():
    data = request.json
    
    if not data:
        return jsonify({"error": "Payload cannot be empty"}), 400

    products = ProductService.create_product(data)

    if not isinstance(products, list):
        return jsonify(products), 400

    response = {
        "message": "Product successfully created",
        "products": [product.to_dict() for product in products]
    }

    return jsonify(response)


@product_bp.route("/products/<string:sku>", methods=["DELETE"])
def delete_product(sku):
    result, products = ProductService.delete_product(sku) 
    
    if not result:
        return jsonify({"error": "Product not found"}), 404
    
    response = {
        "message": f"Product with sku {sku} successfully deleted.",
        "products": [product.to_dict() for product in products]
    }
    return jsonify(response)
