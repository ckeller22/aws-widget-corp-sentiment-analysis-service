import pytest
from app import create_app

TEST = "test"


@pytest.fixture(scope="session")
def app():
    app = create_app("testing")

    yield app


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def runner(app):
    return app.test_cli_runner()
