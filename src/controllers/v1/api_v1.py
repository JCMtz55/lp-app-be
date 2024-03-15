from flask import Blueprint
from flask_cors import CORS

from src.controllers.v1.record_controller import record
from src.controllers.v1.operations_controller import operation

# main blueprint to be registered with application
v1 = Blueprint('v1', __name__)
CORS(v1)

# register user with api blueprint
v1.register_blueprint(record, url_prefix="/record")
v1.register_blueprint(operation, url_prefix="/operation")
