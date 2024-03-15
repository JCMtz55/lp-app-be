from flask import Flask
import os

from flask_cors import CORS

from src.config.config import Config
from dotenv import load_dotenv
from src.extensions import db


def create_app():
    # loading environment variables
    load_dotenv()

    # declaring flask application
    app = Flask(__name__)
    CORS(app)

    # calling the dev configuration
    config = Config().dev_config

    # making our application to use dev env
    app.env = config.ENV

    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("SQLALCHEMY_DATABASE_URI_DEV")
    db.app = app
    db.init_app(app)

    # import api blueprint to register it with app
    from src.routes import api
    app.register_blueprint(api, url_prefix="/api")

    return app

