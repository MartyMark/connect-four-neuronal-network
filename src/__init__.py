from flask import Flask, Blueprint

bp = Blueprint('bp', __name__)


def create_app():
    app = Flask(__name__)

    app.register_blueprint(bp)

    return app
