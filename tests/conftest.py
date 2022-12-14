import pytest

from src.main import app


@pytest.fixture()
def test_client():
    with app.test_client() as testing_client:
        with app.app_context():
            yield testing_client
