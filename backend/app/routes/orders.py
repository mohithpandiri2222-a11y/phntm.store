from flask import Blueprint, jsonify

orders_bp = Blueprint('orders', __name__, url_prefix='/api/orders')

@orders_bp.route('/', methods=['GET'])
def index():
    return jsonify({"success": True, "message": "Orders route initialized"}), 200
