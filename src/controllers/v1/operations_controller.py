from flask import request, jsonify, Blueprint
from flask_cors import cross_origin, CORS

from src.middlewares.auth_middleware import token_required
from src.services.operation_service import get_operations

operation = Blueprint("operation", __name__)
CORS(operation)

@operation.route('/', methods=["GET"])
@token_required
def get_all_operations(current_user):
    try:
        res = get_operations()
        return jsonify(res), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500
