from flask import Blueprint, jsonify

products_bp = Blueprint('products', __name__, url_prefix='/api/products')

@products_bp.route('/', methods=['GET'])
def index():
    return jsonify({"success": True, "message": "Products route initialized"}), 200
