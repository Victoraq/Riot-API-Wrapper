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
                            .format(region,
                                    ', '.join(list(REGION_URL.keys()))))

        self.headers = {"X-Riot-Token": user_api_key}

    def summoner_champion_mastery(self, account_id, champion_id=None):
        """Get champion mastery entries by player id.
        For a specific champion use the champion_id parameter"""

        if champion_id:
            url = API_PATH["champion_mastery"].format(
                region_url=self.region_url,
                account_id=account_id,
                championId=champion_id)
        else:
            url = API_PATH["champion_masteries"].format(
                region_url=self.region_url, account_id=account_id)

        response = requests.get(url, headers=self.headers)

        return response.json()

    def summoner_mastery_score(self, account_id):
        """Get a player's total champion mastery score,
        which is the sum of individual champion mastery levels."""

        url = API_PATH["mastery_score"].format(
            region_url=self.region_url, account_id=account_id)

        response = requests.get(url, headers=self.headers)

        return response.json()

    def champion_rotations(self):
        """Returns champion rotations, including
        free-to-play and low-level free-to-play rotations"""

        url = API_PATH["champion_rotations"].format(region_url=self.region_url)

        response = requests.get(url, headers=self.headers)

        return response.json()
