from app.models.prediction_response import PredictionResponse
from pydantic import ValidationError
from unittest.mock import patch
import pytest
from flask import current_app

POSITIVE_REVIEW = "This movie was very good. I really liked it."
NEGATIVE_REVIEW = "This movie was terrible. I hated it."
POSITIVE_SENTIMENT = "pos"
NEGATIVE_SENTIMENT = "neg"
SENTIMENT = "sentiment"
MESSAGE = "message"
INPUT = "input"


def mock_get_sentiment(input):
    return POSITIVE_SENTIMENT


def test_bad_request_if_request_schema_invalid(client):
    payload = {"bad_key": "bad_value"}
    response = client.post("/predict", json=payload)

    assert response.status_code == 400
    assert (
        response.get_json()[MESSAGE]
        == "The request body does not match the expected schema"
    )


def test_response_returns_prediction_response_type(client, monkeypatch):
    payload = {INPUT: POSITIVE_REVIEW}

    # Mock the get_sentiment method of the PredictionService
    # App context needs to be used to be able to access current_app.
    with client.application.app_context():
        monkeypatch.setattr(
            "app.predict.routes.current_app.prediction_service.get_sentiment",
            mock_get_sentiment,
        )

        response = client.post("/predict", json=payload)

    assert response.status_code == 200
    assert PredictionResponse.model_validate(response.get_json())
    assert response.get_json()[SENTIMENT] == POSITIVE_SENTIMENT
