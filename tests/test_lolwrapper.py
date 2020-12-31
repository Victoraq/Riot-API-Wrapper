from lolwrapper.lolwrapper import LoLWrapper
from lolwrapper.const import (
    REGION_URL, QUEUE_LIST, TIER_LIST, DIVISION_LIST
)
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
    wrapper = LoLWrapper(environment['api_key'], region="BR1")

    return wrapper


def test_wrong_region():
    """Tests the exception raised after try to initialize
    the wrapper with a not available region"""

    region = "WRONG"

    with pytest.raises(Exception) as region_info:
        _ = LoLWrapper("key", region=region)

    assert f"{region} is not available" in str(region_info.value)
    assert ', '.join(list(REGION_URL.keys())) in str(region_info.value)


def test_get_summoner_by_id(wrapper, environment):
    """Tests an API call to get a summoner by the id"""

    summoner_id = environment['summoner_id']
    response = wrapper.summoner_by_id(summoner_id)

    assert isinstance(response, dict)
    assert "id" in response.keys()
    assert response["id"] == summoner_id
    assert "puuid" in response.keys()
    assert "accountId" in response.keys()


def test_summoner_champion_mastery_list(wrapper, environment):
    """Tests an API call to get the all champion mastery`s of a summoner"""

    summoner_id = environment['summoner_id']
    response = wrapper.summoner_champion_mastery(summoner_id)

    assert isinstance(response, list)
    assert isinstance(response[0], dict)
    assert response[0]["summonerId"] == summoner_id


def test_summoner_champion_mastery(wrapper, environment):
    """Tests an API call to get a champion mastery of a summoner"""

    summoner_id = environment['summoner_id']
    champion_id = 43
    response = wrapper.summoner_champion_mastery(summoner_id, champion_id)

    assert isinstance(response, dict)
    assert response["championId"] == champion_id
    assert response["summonerId"] == summoner_id


def test_summoner_mastery_score(wrapper, environment):
    """Tests an API call to get a mastery score of a summoner"""

    summoner_id = environment['summoner_id']

    response = wrapper.summoner_mastery_score(summoner_id)

    assert isinstance(response, int)


def test_champion_rotations(wrapper):
    """Test an API call to get the champion rotation"""

    response = wrapper.champion_rotations()

    assert isinstance(response, dict)
    assert "freeChampionIds" in response.keys()
    assert "freeChampionIdsForNewPlayers" in response.keys()


def test_league_entries(wrapper):
    """Test an API call to get all league entries"""

    queue = "RANKED_SOLO_5x5"
    tier = "CHALLENGER"
    division = "I"

    response = wrapper.league_entries(queue, tier, division)

    assert isinstance(response, list)
    assert isinstance(response[0], dict)
    assert "leagueId" in response[0]


def test_league_entries_page(wrapper):
    """Test an API call to get league entries by page"""

    queue = "RANKED_SOLO_5x5"
    tier = "BRONZE"
    division = "I"
    page = 2

    response_page1 = wrapper.league_entries(queue, tier, division)
    response_page2 = wrapper.league_entries(queue, tier, division, page=page)

    assert isinstance(response_page2, list)
    assert response_page1 != response_page2


def test_league_entries_wrong_parameter_message(wrapper):
    """Test an API call to get league entries by page"""

    queue = "RANKED_SOLO_5x5"
    wrong_queue = "RANKED_DUO_5x5"
    tier = "BRONZE"
    wrong_tier = "MASTERY"
    division = "I"
    wrong_division = "VIIII"

    # queue message
    with pytest.raises(Exception) as queue_info:
        _ = wrapper.league_entries(wrong_queue, tier, division)

    assert f"{wrong_queue} is not available" in str(queue_info.value)
    assert ', '.join(QUEUE_LIST) in str(queue_info.value)

    # tier message
    with pytest.raises(Exception) as tier_info:
        _ = wrapper.league_entries(queue, wrong_tier, division)

    assert f"{wrong_tier} is not available" in str(tier_info.value)
    assert ', '.join(TIER_LIST) in str(tier_info.value)

    # division message
    with pytest.raises(Exception) as division_info:
        _ = wrapper.league_entries(queue, tier, wrong_division)

    assert f"{wrong_division} is not available" in str(division_info.value)
    assert ', '.join(DIVISION_LIST) in str(division_info.value)


def test_match_list(wrapper, environment):
    """Test an API call to get the match list of a user"""

    summoner_id = environment['summoner_id']

    # get the account_id
    user_data = wrapper.summoner_by_id(summoner_id)

    account_id = user_data["accountId"]

    response = wrapper.match_list(account_id)

    assert isinstance(response, dict)
    assert "matches" in response.keys()
    assert isinstance(response["matches"], list)
    assert isinstance(response["matches"][0], dict)
    assert "gameId" in response["matches"][0].keys()




def test_match_by_id(wrapper, environment):
    """Test an API call to get a match by id"""

    summoner_id = environment['summoner_id']

    # get the account_id
    user_data = wrapper.summoner_by_id(summoner_id)

    account_id = user_data["accountId"]

    match_list = wrapper.match_list(account_id)

    game_id = match_list["matches"][0]["gameId"]

    response = wrapper.match_by_id(game_id)

    assert isinstance(response, dict)
    assert "gameId" in response.keys()
    assert response["gameId"] == game_id
    assert "mapId" in response.keys()

