from flask import Blueprint, jsonify

health_bp = Blueprint('health', __name__, url_prefix='/api/health')

@health_bp.route('/', methods=['GET'])
def index():
    return jsonify({"success": True, "message": "Backend is running"}), 200
