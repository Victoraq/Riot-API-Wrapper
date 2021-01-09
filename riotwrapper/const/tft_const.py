# flake8: noqa
# fmt: off

"""List of Teamfight Tactics API available regions and endpoints."""

MATCH_REGION_URL = {
    "AMERICAS": "https://americas.api.riotgames.com",
    "ASIA": "https://asia.api.riotgames.com",
    "EUROPE": "https://europe.api.riotgames.com",
}

# the users are the same of LoL, so they share the same regions

AMERICAS = ["BR1", "LA1", "LA2", "NA1", "OC1"]
ASIA = ["JP1", "KR"]
EUROPE = ["RU", "EUN1", "TR1"]

USER_REGION_URL = {
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
    "match_ids": "{region_url}/tft/match/v1/matches/by-puuid/{account_id}/ids",
    "match_by_id": "{region_url}/tft/match/v1/matches/{matchId}",
}
