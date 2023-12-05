from flask import Flask

from config import Config
from app.services import PredictionService


def create_app(config_name):
    app = Flask(__name__)

    config_module = f"config.{config_name.capitalize()}Config"

    app.config.from_object(config_module)

    app.prediction_service = PredictionService()

    from app.main import bp as main_bp
    from app.predict import bp as predict_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(predict_bp)

    @app.route("/whale")
    def test_page():
        return "<h1>Whale, Hello there!</h1>"

    return app
