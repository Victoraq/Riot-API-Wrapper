import pytest


@pytest.fixture
def environment():
    import os

    api_key = os.environ.get('API_KEY')

    env = {
        'api_key': api_key,
    }

    return env
