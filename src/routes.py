from flask import Blueprint
from src.controllers.v1.api_v1 import v1
from src.controllers.v2.api_v2 import v2

# main blueprint to be registered with application
api = Blueprint('api', __name__)

# register user with api blueprint
api.register_blueprint(v1, url_prefix="/v1")
api.register_blueprint(v2, url_prefix="/v2")