from flask import Blueprint

bp = Blueprint("predict", __name__)

from app.predict import routes
