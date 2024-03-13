from flask import Blueprint
from src.controllers.v2.record_controller import record

# main blueprint to be registered with application
v2 = Blueprint('v2', __name__)

# register user with api blueprint
v2.register_blueprint(record, url_prefix="/record")