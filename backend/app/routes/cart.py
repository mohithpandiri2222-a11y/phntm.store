from flask import Blueprint, jsonify

cart_bp = Blueprint('cart', __name__, url_prefix='/api/cart')

@cart_bp.route('/', methods=['GET'])
def index():
    return jsonify({"success": True, "message": "Cart route initialized"}), 200
