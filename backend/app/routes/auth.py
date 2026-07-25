from flask import Blueprint, jsonify

auth_bp = Blueprint('auth', __name__, url_prefix='/api/auth')

@auth_bp.route('/', methods=['GET'])
def index():
    return jsonify({"success": True, "message": "Auth route initialized"}), 200
