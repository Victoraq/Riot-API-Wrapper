"""List of Riot API available endpoints."""

# flake8: noqa
# fmt: off
API_PATH = {
    "champion_masteries": "{region_url}/lol/champion-mastery/v4/champion-masteries/by-summoner/{account_id}",
    "champion_mastery": "{region_url}/lol/champion-mastery/v4/champion-masteries/by-summoner/{account_id}/by-champion/{championId}",
    "mastery_score": "{region_url}/lol/champion-mastery/v4/scores/by-summoner/{account_id}",
    "champion_rotations": "{region_url}/lol/platform/v3/champion-rotations",
}