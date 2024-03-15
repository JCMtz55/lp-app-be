from flask import jsonify, Blueprint

from src.middlewares.auth_middleware import token_required

record = Blueprint("record", __name__)


@record.route('/', methods=["GET"])
@token_required
def get_records(current_user):
    return jsonify("To be Implemented"), 201


@record.route('/create', methods=["POST"])
@token_required
def create_record(current_user):
    return jsonify("To be Implemented"), 201

@record.route('/delete', methods=["PUT"])
@token_required
def delete_record(current_user, record_id):
    return jsonify("To be Implemented"), 201


