from flask import Blueprint
from src.controllers.v1.record_controller import record

# main blueprint to be registered with application
v1 = Blueprint('v1', __name__)

# register user with api blueprint
v1.register_blueprint(record, url_prefix="/record")