# flake8: noqa
# fmt: off

"""List of Legends of Runeterra API available regions and endpoints."""

REGION_URL = {
    "AMERICAS": "https://americas.api.riotgames.com",
    "ASIA": "https://asia.api.riotgames.com",
    "EUROPE": "https://europe.api.riotgames.com",
}

API_PATH = {
    "platform_data": "{region_url}/lor/status/v1/platform-data",
    "match_ids": "{region_url}/lor/match/v1/matches/by-puuid/{account_id}/ids",
    "match_by_id": "{region_url}/lor/match/v1/matches/{match_id}",
    "leaderboard": "{region_url}/lor/ranked/v1/leaderboards",
}
