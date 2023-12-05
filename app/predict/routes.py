from flask import request, jsonify, Response
from app.predict import bp
from pydantic import ValidationError
from app.models.PredictionRequest import PredictionRequest
from app.models.PredictionResponse import PredictionResponse


@bp.route("/predict", methods=["POST"])
def predict():
    try:
        payload = PredictionRequest.model_validate(request.json)
    except ValidationError as e:
        return {
            "message": "The request body does not match the expected schema",
            "errors": e.errors(),
        }, 400

    response = PredictionResponse(sentiment="positive")

    return response.model_dump()
