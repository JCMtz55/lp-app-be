from flask import request, jsonify, Blueprint
from flask_cors import CORS

from src.middlewares.auth_middleware import token_required
from src.services.record_service import insert_record, get_user_records, delete_user_record, refund_user_record
from src.dtos.operation_dto import OperationRequest


record = Blueprint("record", __name__)
CORS(record)

@record.route('/', methods=["GET"])
@token_required
def get_records(current_user):
    try:
        res = get_user_records(current_user)
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

@record.route('/delete', methods=["POST"])
@token_required
def delete_record(current_user):
    record_id = request.get_json()['record_id']
    try:
        deleted = delete_user_record(record_id)
        if deleted is True:
            res = refund_user_record(current_user, record_id)
            return jsonify(res), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500


