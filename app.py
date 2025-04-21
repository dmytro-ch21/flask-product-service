from flask import Flask, jsonify, render_template, request
from controllers.product_controller import product_bp

def create_app():
    app = Flask(__name__)
    app.register_blueprint(product_bp)
    
    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({"error": "Bad Request"}), 400
    
    @app.errorhandler(404)
    def not_found(error):
        return jsonify({"error": "Not Found"}), 404
    
    @app.errorhandler(500)
    def internal_error(error):
        return jsonify({"error": "Internal Server Error"}), 500
    
    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)

