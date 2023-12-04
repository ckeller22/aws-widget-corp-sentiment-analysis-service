from flask import Flask

from config import Config

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    @app.route('/')
    def test_page():
        return '<h1>Whale, Hello there!</h1>'

    return app