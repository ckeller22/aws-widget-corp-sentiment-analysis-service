from app.services import PredictionService


def test_service_should_load_model_file():
    service = PredictionService()
    assert service.model is not None
