# first import the nececessary modules
from flask import Flask, jsonify, render_template, request

# instantiate the Flask() class and assign to a variable
app = Flask(__name__)

# data source
products = [
    {"sku": "001", "name": "Dell Laptop XP500", "price": 1299.99, "quantity": 10, "description": "A high-performance laptop - Intel i7 - Nvidia GTX 5080 - 32GB"},
    {"sku": "002", "name": "iPhone 16 Pro", "price": 899.99, "quantity": 100, "description": "High quality smartphone"},
    {"sku": "003", "name": "Headphones - Beats", "price": 299.99, "quantity": 200, "description": "Great headphones for workouts"},
]

# create the default route ("/")
# by def the route works as GET request
@app.route("/")
def home():
    return render_template("index.html")

# the route that returnds all the products
# it should be get and return multiple producs
@app.route("/api/products", methods=["GET"])
def get_products():
    return jsonify(products)

# we need a route/endpoint that will return us a spesific product
# to accept in endpoints a path parameter 
# we use the <> and inside we can specify the data type we expect this to be 
# we can have: string, int, float etc...
# then we use a column and provide a placeholder that will be used for that parameter
@app.route("/api/products/<string:sku>", methods=["GET"])
def get_product(sku):
    print(f"Data recieved as sku: {sku}")
    for product in products:
        if sku == product.get("sku"):
            return jsonify(product), 200
    return jsonify({"error": f"The product with sku {sku} not found."}), 404  


@app.route("/api/products", methods=["POST"])
def add_product():
    """
    Request Body
    {
        "sku": str*, 
        "name": str*, 
        "price": float, 
        "quantity": int, 
        "description": str
    }
    """
    # access the data from request
    new_product = request.json # the json will throw an error
    # once you have the record it is important to validate if the required parts are present
    if not new_product:
        return jsonify({"error": "The payload cannot be empty"}), 400
    # check if sku and name are present in the body
    if "sku" not in new_product or "name" not in new_product:
        return jsonify({"error": "Fields name and sku are required."}), 400
    # check if we already have a sku that is passed in body
    for product in products:
        if new_product.get("sku") == product.get("sku"):
            return jsonify({"error": f"sku {new_product.get("sku")} is already present"}), 400
        
    print(f"===== Type of the product name: {type(new_product).__name__}")
       
    if type(new_product.get("name")).__name__ != "str":
        return jsonify({"error": "Field name should be a string"}), 400
            
    # if none of the above have failed then we append to products
    products.append(new_product)
    # and return back a response with SC 201
    return jsonify({"status": f"Sccessfully created product with sku {new_product.get("sku")}", "products": products}), 201


@app.route("/api/products/<string:sku>", methods=["PUT"])
def update_product(sku):
    product_update = None
    for product in products:
        if sku == product.get("sku"):
            product_update = product

    if product_update:
        new_product = request.json
        product_update.update(new_product)
        return jsonify({"status": "product successfully updated", "products": products})

    return jsonify({"error": "Product not found"}), 400


@app.route("/api/products/<string:sku>", methods=["DELETE"])
def delete_product(sku):
    product_delete = None
    for product in products: 
        if sku == product.get("sku"):
            product_delete = product

    if product_delete:
       products.remove(product_delete)
       return jsonify({"status": "successfully deleted", "products": products})  

    return jsonify({"error": "Product not found"})



if __name__ == "__main__":
    app.run(debug=True)

