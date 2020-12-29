import requests
from lolwrapper.const import (
    API_PATH, REGION_URL, QUEUE_LIST,
    TIER_LIST, DIVISION_LIST
)


class LoLWrapper():

    def __init__(self, api_key, region):
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

    def league_entries(self, queue, tier, division, page=None):
        """Get all the league entries.
        The entries can be devided into pages.
        If not provide the page parameter it will start at page 1.

        The possible parameter values are:

        Queue: RANKED_SOLO_5x5, RANKED_FLEX_SR,
            RANKED_FLEX_TFT, RANKED_FLEX_TT

        Tier: IRON, BRONZE, SILVER, GOLD, PLATINUM, DIAMOND,
            MASTER, GRANDMASTER, CHALLENGER

        Division: I, II, III, IV
        """

        if queue not in QUEUE_LIST:
            raise Exception("""
                The queue {} is not available.
                The currently available queues are: {}"""
                            .format(queue, ', '.join(QUEUE_LIST)))

        if tier not in TIER_LIST:
            raise Exception("""
                The tier {} is not available.
                The currently available tiers are: {}"""
                            .format(tier, ', '.join(TIER_LIST)))

        if division not in DIVISION_LIST:
            raise Exception("""
                The division {} is not available.
                The currently available divisions are: {}"""
                            .format(division, ', '.join(DIVISION_LIST)))

        url = API_PATH["league_entries"].format(
            region_url=self.region_url,
            queue=queue,
            tier=tier,
            division=division)

        if page:
            url += f"?page={page}"

        response = requests.get(url, headers=self.headers)

        return response.json()
