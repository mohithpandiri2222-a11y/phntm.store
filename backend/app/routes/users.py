from flask import Blueprint, jsonify

users_bp = Blueprint('users', __name__, url_prefix='/api/users')

@users_bp.route('/', methods=['GET'])
def index():
    return jsonify({"success": True, "message": "Users route initialized"}), 200
