from flask import Flask
import os
from src.config.config import Config
from dotenv import load_dotenv
from flask_bcrypt import Bcrypt

# loading environment variables
load_dotenv()

# declaring flask application
app = Flask(__name__)

# calling the dev configuration
config = Config().dev_config

# making our application to use dev env
app.env = config.ENV

# load the secret key defined in the .env file
app.secret_key = os.environ.get("SECRET_KEY")
bcrypt = Bcrypt(app)

# import api blueprint to register it with app
from src.routes import api
app.register_blueprint(api, url_prefix="/api")

