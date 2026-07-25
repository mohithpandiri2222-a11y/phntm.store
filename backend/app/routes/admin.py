from flask import Blueprint, jsonify

admin_bp = Blueprint('admin', __name__, url_prefix='/api/admin')

@admin_bp.route('/', methods=['GET'])
def index():
    return jsonify({"success": True, "message": "Admin route initialized"}), 200
