# flake8: noqa
# fmt: off

"""List of Riot API available regions and endpoints."""

REGION_URL = {
    "BR1": "https://br1.api.riotgames.com",
    "EUN1": "https://eun1.api.riotgames.com",
    "JP1": "https://jp1.api.riotgames.com",
    "KR": "https://kr.api.riotgames.com",
    "LA1": "https://la1.api.riotgames.com",
    "LA2": "https://la2.api.riotgames.com",
    "NA1": "https://na1.api.riotgames.com",
    "OC1": "https://oc1.api.riotgames.com",
    "RU": "https://ru.api.riotgames.com",
    "TR1": "https://tr1.api.riotgames.com",
}

API_PATH = {
    "champion_masteries": "{region_url}/lol/champion-mastery/v4/champion-masteries/by-summoner/{account_id}",
    "champion_mastery": "{region_url}/lol/champion-mastery/v4/champion-masteries/by-summoner/{account_id}/by-champion/{championId}",
    "mastery_score": "{region_url}/lol/champion-mastery/v4/scores/by-summoner/{account_id}",
    "champion_rotations": "{region_url}/lol/platform/v3/champion-rotations",
    "league_entries": "{region_url}/lol/league-exp/v4/entries/{queue}/{tier}/{division}",
}

"""Lists of queue, tiers and divisions available"""

QUEUE_LIST = ["RANKED_SOLO_5x5", "RANKED_FLEX_SR", "RANKED_FLEX_TFT", "RANKED_FLEX_TT"]

TIER_LIST = ["IRON", "BRONZE", "SILVER", "GOLD", "PLATINUM", "DIAMOND", "MASTER", "GRANDMASTER", "CHALLENGER"]

DIVISION_LIST = ["I", "II", "III", "IV"]