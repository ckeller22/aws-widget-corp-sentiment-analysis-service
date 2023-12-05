from app.models.PredictionResponse import PredictionResponse
from pydantic import ValidationError


def test_bad_request_if_request_schema_invalid(client):
    payload = {"bad_key": "bad_value"}
    response = client.post("/predict", json=payload)

    assert response.status_code == 400
    assert (
        response.get_json()["message"]
        == "The request body does not match the expected schema"
    )


def test_response_returns_prediction_response_type(client):
    payload = {"input": "This movie was very good."}
    response = client.post("/predict", json=payload)

    assert response.status_code == 200
    assert PredictionResponse.model_validate(response.get_json())
