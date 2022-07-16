import pytest
import run


# Creating a fixture for testing all views (main, candidates, vacancies)
@pytest.fixture()
def test_client():
    app = run.app
    return app.test_client()
