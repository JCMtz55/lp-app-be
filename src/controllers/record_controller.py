from flask import request, jsonify, Blueprint

from src.middlewares.auth_middleware import token_required
from src.services.record_service import insert_record, get_user_records
from src.models.operation_dto import OperationRequest
from src.models.record_dto import RecordRequest

record = Blueprint("record", __name__)


@record.route('/', methods=["GET"])
@token_required
def get_records(current_user):
    data = request.get_json()
    req = RecordRequest(data)
    try:
        res = get_user_records(current_user, req)
        return jsonify(res), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@record.route('/create', methods=["POST"])
@token_required
def create_record(current_user):
    data = request.get_json()
    operation_req = OperationRequest(data)
    try:
        res = insert_record(current_user, operation_req)
        return jsonify(res), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@record.route('/delete', methods=["PUT"])
@token_required
def delete_record(current_user, record_id):
    return jsonify(""), 201


