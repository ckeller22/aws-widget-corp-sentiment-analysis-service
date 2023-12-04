from flask import Flask

from config import Config

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    @app.route('/whale')
    def test_page():
        return '<h1>Whale, Hello there!</h1>'

    return app