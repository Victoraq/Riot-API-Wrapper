import requests
from .const import REGION_URL, API_PATH


class LoLWrapper():

    def __init__(self, api_key, region):
        user_api_key = api_key

        if region in REGION_URL.keys():
            self.region_url = REGION_URL[region]
        else:
            raise Exception("""
                The region {} is not available. 
                The current available regions are: {}"""
                .format(region, ', '.join(list(REGION_URL.keys()))))
                
        self.headers = {"X-Riot-Token": user_api_key}

    def summoner_champion_mastery(self, account_id=None):
        url = API_PATH["champion_masteries"].format(
            region_url=self.region_url, account_id=account_id)

        response = requests.get(url, headers=self.headers)

        return response.json()
    
