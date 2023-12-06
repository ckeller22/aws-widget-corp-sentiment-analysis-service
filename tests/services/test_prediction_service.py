import pytest

from app.services import PredictionService


@pytest.fixture(scope="module")
def service():
    return PredictionService()


def test_service_should_load_model_file(service):
    assert service.model is not None


def test_service_should_load_nltk_resources(service):
    assert service.stopword_list is not None
    assert service.stemmer is not None


def test_service_should_return_positive_sentiment(service):
    data = {"review": "I love this movie"}
    result = service.predict(data)
    assert result["sentiment"] == "positive"
