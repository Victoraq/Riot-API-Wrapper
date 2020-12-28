from lolwrapper.lolwrapper import LoLWrapper
from lolwrapper.const import REGION_URL
import pytest

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

def test_wrong_region():
    """Tests the exception raised after try to initialize the wrapper with a not available region"""

    region = "WRONG"

    with pytest.raises(Exception) as region_info:
        wrapper = LoLWrapper("key", region=region)

    assert f"{region} is not available" in str(region_info.value)
    assert ', '.join(list(REGION_URL.keys())) in str(region_info.value)


def test_summoner_champion_mastery(environment):
    """Tests an API call to get the all champion mastery`s of a summoner"""

    wrapper = LoLWrapper(environment['api_key'], region="BR1")

    account_id = environment['account_id']
    response = wrapper.summoner_champion_mastery(account_id)

    assert isinstance(response, list)
    assert isinstance(response[0], dict)
    assert response[0]["summonerId"] == account_id
