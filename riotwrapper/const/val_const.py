# flake8: noqa
# fmt: off

"""List of Valorant API available regions and endpoints."""

REGION_URL = {
    "BR": "https://br.api.riotgames.com",
    "EUN": "https://eun.api.riotgames.com",
    "AP": "https://ap.api.riotgames.com",
    "KR": "https://kr.api.riotgames.com",
    "LATAM": "https://latam.api.riotgames.com",
    "NA": "https://na.api.riotgames.com",
}


API_PATH = {
    "platform_data": "{region_url}/val/status/v1/platform-data",
    "contents": "{region_url}/val/status/v1/contents",
}