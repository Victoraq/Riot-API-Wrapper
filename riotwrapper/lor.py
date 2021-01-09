import requests
from riotwrapper.const.lor_const import (
    REGION_URL, API_PATH
)


class LoRWrapper():

    def __init__(self, api_key, region):
        """Legends of Runeterra API Wrapper

        :param api_key: Riot Developer API Key.
        :param region: The region to execute the requests.

        """

        user_api_key = api_key

        if region in REGION_URL.keys():
            self.region_url = REGION_URL[region]
        else:
            raise Exception("""
                The region {} is not available.
                The currently available regions are: {}"""
                            .format(region,
                                    ', '.join(list(REGION_URL.keys()))))

        self.headers = {"X-Riot-Token": user_api_key}

    def platform_data(self):
        """Get Legends of Runeterra status for the region."""

        url = API_PATH["platform_data"].format(region_url=self.region_url)

        response = requests.get(url, headers=self.headers)

        return response.json()

    def match_by_id(self, match_id):
        """Get match by id.

        :param match_id: Match ID code.

        """

        url = API_PATH["match_by_id"].format(
            region_url=self.region_url, match_id=match_id)

        response = requests.get(url, headers=self.headers)

        return response.json()

    def match_ids(self, account_id):
        """Get match id list by account id.

        :param account_id: Account ID or PUUID code.

        """

        url = API_PATH["match_ids"].format(
            region_url=self.region_url, account_id=account_id)

        response = requests.get(url, headers=self.headers)

        return response.json()

    def leaderboard(self):
        """Get the players in Master tier."""

        url = API_PATH["leaderboard"].format(region_url=self.region_url)

        response = requests.get(url, headers=self.headers)

        return response.json()
