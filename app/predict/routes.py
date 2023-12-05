from flask import request, jsonify, Response
from app.predict import bp
from pydantic import ValidationError
from app.models.prediction_request import PredictionRequest
from app.models.prediction_response import PredictionResponse


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
