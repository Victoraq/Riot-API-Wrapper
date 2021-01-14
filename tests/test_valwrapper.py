from riotwrapper.val import ValWrapper
from riotwrapper.const.val_const import (
    REGION_URL
)
import pytest


@pytest.fixture
def environment():
    import os

    api_key = os.environ.get('API_KEY')

    env = {
        'api_key': api_key,
    }

    return env


@pytest.fixture
def wrapper(environment):
    wrapper = ValWrapper(environment['api_key'], region="BR")

    return wrapper


class TestValWrapper():

    def test_wrong_region(self):
        """Tests the exception raised after try to initialize
        the wrapper with a not available region"""

        region = "WRONG"

        with pytest.raises(Exception) as region_info:
            _ = ValWrapper("key", region=region)

        assert f"{region} is not available" in str(region_info.value)
        assert ', '.join(list(REGION_URL.keys())) in str(region_info.value)

    def test_platform_data(self, wrapper):
        """Tests an API call to get platform data."""

        response = wrapper.platform_data()

        assert isinstance(response, dict)
        assert "id" in response.keys()
        assert "maintenances" in response.keys()
        assert "incidents" in response.keys()
