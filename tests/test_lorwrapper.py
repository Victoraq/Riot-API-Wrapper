from riotwrapper.lor import LoRWrapper
from riotwrapper.const.lor_const import REGION_URL
import pytest
import re


@pytest.fixture
def environment():
    import os

    api_key = os.environ.get('API_KEY')
    account_id = os.environ.get('ACCOUNT_ID')

    env = {
        'api_key': api_key,
        'account_id': account_id
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

    def test_match_ids(self, wrapper, environment):
        """Tests an API call to get the match id list by user."""

        account_id = environment['account_id']

        response = wrapper.match_ids(account_id)

        pattern = re.compile(r'^(\w+\-\w+\-\w+\-\w+\-\w+)$')

        assert isinstance(response, list)
        assert pattern.match(response[0])

    def test_match_by_id(self, wrapper, environment):
        """Tests and API call to get a match by id."""

        account_id = environment['account_id']

        match_list = wrapper.match_ids(account_id)

        match_id = match_list[0]

        response = wrapper.match_by_id(match_id)

        assert isinstance(response, dict)
        assert "metadata" in response.keys()
        assert "info" in response.keys()
