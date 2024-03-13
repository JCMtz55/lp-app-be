from flask import Blueprint
from src.controllers.record_controller import record

# main blueprint to be registered with application
api = Blueprint('api', __name__)

# register user with api blueprint
api.register_blueprint(record, url_prefix="/record")