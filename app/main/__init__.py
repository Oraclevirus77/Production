from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_cors import CORS


from app.main.config import config_by_name


db = SQLAlchemy()
flask_bcrypt = Bcrypt()


app = Flask(__name__)
cors = CORS(app)


def create_app(config_name):
    with app.app_context():
        app.config.from_object(config_by_name[config_name])
        db.init_app(app)
        flask_bcrypt.init_app(app)
    return app
