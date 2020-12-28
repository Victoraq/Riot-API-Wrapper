"""List of Riot API available regions and endpoints."""

# flake8: noqa
# fmt: off
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
}