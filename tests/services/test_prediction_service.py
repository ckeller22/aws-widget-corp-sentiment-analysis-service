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


def test_get_sentiment_should_return_sentiment(service):
    data = "Avatar The Last Airbender is the a movie that should have never been made. It is a disgrace to the original series."
    result = service.get_sentiment(data)
    assert isinstance(result, str)


def test_bag_of_words_should_return_empty_dict_when_given_empty_list(service):
    words = []
    result = service.bag_of_words(words)
    assert result == {}


def test_bag_of_words_should_return_correct_bag_of_words(service):
    words = ["apple", "banana", "apple", "cherry"]
    result = service.bag_of_words(words)
    expected = {"apple": 2, "banana": 1, "cherry": 1}
    assert result == expected
