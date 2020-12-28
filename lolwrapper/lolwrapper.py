import requests
from .endpoints import API_PATH


class LoLWrapper():

    _region_dict = {
        "BR1": "https://br1.api.riotgames.com"
    }

    def __init__(self, api_key, region):
        user_api_key = api_key
        self.region_url = self._region_dict[region]
        self.headers = {"X-Riot-Token": user_api_key}

    def summoner_champion_mastery(self, account_id=None):
        url = API_PATH["champion_masteries"].format(
            region_url=self.region_url, account_id=account_id)

        response = requests.get(url, headers=self.headers)

        return response.json()
    
