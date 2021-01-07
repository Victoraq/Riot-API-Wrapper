from riotwrapper.lor import LoRWrapper
from riotwrapper.const.lor_const import REGION_URL
import pytest


@pytest.fixture
def environment():
    import os

    api_key = os.environ.get('API_KEY')
    summoner_id = os.environ.get('SUMMONER_ID')

    env = {
        'api_key': api_key,
        'summoner_id': summoner_id
    }

    return env


@pytest.fixture
def wrapper(environment):
    wrapper = LoRWrapper(environment['api_key'], region="AMERICAS")

    return wrapper


class TestLoRWrapper:

    def test_wrong_region(self):
        """Tests the exception raised after try to initialize
        the wrapper with a not available region"""

        region = "WRONG"

        with pytest.raises(Exception) as region_info:
            _ = LoRWrapper("key", region=region)

        assert f"{region} is not available" in str(region_info.value)
        assert ', '.join(list(REGION_URL.keys())) in str(region_info.value)

    def test_platform_data(self, wrapper):
        """Tests an API call to get platform data."""

        response = wrapper.platform_data()

        assert isinstance(response, dict)
        assert "id" in response.keys()
        assert "maintenances" in response.keys()
        assert "incidents" in response.keys()

    def test_leaderboard(self, wrapper):
        """Tests an API call to get the leaderboard."""

        response = wrapper.leaderboard()

        assert isinstance(response, dict)
        assert "players" in response.keys()
        assert isinstance(response["players"], list)
        assert len(response["players"]) > 0
        assert "name" in response["players"][0].keys()
