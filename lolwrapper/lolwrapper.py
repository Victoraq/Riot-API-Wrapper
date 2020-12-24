import requests


class LoLWrapper():

    _region_dict = {
        "BR1": "https://br1.api.riotgames.com"
    }

    def __init__(self, api_key, region):
        user_api_key = api_key
        self.region_url = self._region_dict[region]
        self.headers = {"X-Riot-Token": user_api_key}

    def summoner_champion_mastery(self, account_id=None):
        url = f"{self.region_url}/lol/champion-mastery/v4/champion-masteries/by-summoner/{account_id}"

        response = requests.get(url, headers=self.headers)

        return response.json()
    
