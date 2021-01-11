from riotwrapper.tft import TFTWrapper
from riotwrapper.const.tft_const import (
    USER_REGION_URL, TIER_LIST, HIGH_TIER_LIST
)
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
    wrapper = TFTWrapper(environment['api_key'], region="BR1")

    return wrapper


class TestTFTWrapper:

    def test_wrong_region(self):
        """Tests the exception raised after try to initialize
        the wrapper with a not available region"""

        region = "WRONG"

        with pytest.raises(Exception) as region_info:
            _ = TFTWrapper("key", region=region)

        assert f"{region} is not available" in str(region_info.value)
        assert ', '.join(list(USER_REGION_URL.keys())) in str(region_info.value)

    def test_match_ids(self, wrapper, environment):
        """Tests an API call to get the match id list by user."""

        account_id = environment['account_id']

        response = wrapper.match_ids(account_id)

        pattern = re.compile(r'^\w+_[0-9]+$')

        assert isinstance(response, list)
        assert pattern.match(response[0])

    def test_match_ids_with_count(self, wrapper, environment):
        """Tests an API call to get the match id list by user
            with a count limit."""

        account_id = environment['account_id']

        response = wrapper.match_ids(account_id, count=5)

        assert isinstance(response, list)
        assert len(response) <= 5
    
    def test_match_by_id(self, wrapper, environment):
        """Tests and API call to get a match by id."""

        account_id = environment['account_id']

        match_list = wrapper.match_ids(account_id)

        match_id = match_list[0]

        response = wrapper.match_by_id(match_id)

        assert isinstance(response, dict)
        assert "metadata" in response.keys()
        assert "info" in response.keys()

    def test_league_entries(self, wrapper):
        """Test an API call to get all league entries"""

        tier = "DIAMOND"
        division = "I"

        response = wrapper.league_entries(tier, division)

        assert isinstance(response['entries'], list)
        assert isinstance(response['entries'][0], dict)
        assert "summonerId" in response['entries'][0].keys()

    def test_not_provide_division_league_entries(self, wrapper):
        """Test an API call to get all league entries
           not providing the division."""

        tier = "DIAMOND"

        with pytest.raises(Exception) as wrapper_info:
            _ = wrapper.league_entries(tier)

        assert "division must be provided." in str(wrapper_info.value)
        assert ', '.join(list(TIER_LIST)) in str(wrapper_info.value)

    def test_league_entries_high_tier(self, wrapper):
        """Test an API call to get all league entries from high tiers."""

        response_list = []
        
        for tier in HIGH_TIER_LIST:
            response_list.append(wrapper.league_entries(tier))

        for response in response_list:
            assert isinstance(response['entries'], list)
            assert isinstance(response['entries'][0], dict)
            assert "summonerId" in response['entries'][0].keys()
