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

    def platform_data(self):
        """Get the platform data."""

        url = API_PATH["platform_data"].format(region_url=self.region_url)

        response = requests.get(url, headers=self.headers)

        return response.json()

    def summoner_by_id(self, summoner_id):
        """Get a summoner by summoner ID."""

        url = API_PATH["summoner_by_id"].format(
                region_url=self.region_url, summoner_id=summoner_id)

        response = requests.get(url, headers=self.headers)

        return response.json()

    def summoner_champion_mastery(self, summoner_id, champion_id=None):
        """Get champion mastery entries by player id.
        For a specific champion use the champion_id parameter."""

        if champion_id:
            url = API_PATH["champion_mastery"].format(
                region_url=self.region_url,
                summoner_id=summoner_id,
                championId=champion_id)
        else:
            url = API_PATH["champion_masteries"].format(
                region_url=self.region_url, summoner_id=summoner_id)

        response = requests.get(url, headers=self.headers)

        return response.json()

    def summoner_mastery_score(self, summoner_id):
        """Get a player's total champion mastery score,
        which is the sum of individual champion mastery levels."""

        url = API_PATH["mastery_score"].format(
            region_url=self.region_url, summoner_id=summoner_id)

        response = requests.get(url, headers=self.headers)

        return response.json()

    def champion_rotations(self):
        """Returns champion rotations, including
        free-to-play and low-level free-to-play rotations."""

        url = API_PATH["champion_rotations"].format(region_url=self.region_url)

        response = requests.get(url, headers=self.headers)

        return response.json()

    def summoner_league_entry(self, summoner_id):
        """Get league entries in all queues for a given summoner ID."""

        url = API_PATH["league_entry"].format(
            region_url=self.region_url, summoner_id=summoner_id)

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

    def match_by_id(self, match_id):
        """Get match by match ID."""

        url = API_PATH["match_by_id"].format(
            region_url=self.region_url, match_id=match_id)

        response = requests.get(url, headers=self.headers)

        return response.json()

    def match_list(self, account_id,
                   champion=None,
                   queue=None,
                   season=None,
                   endTime=None,
                   beginTime=None,
                   endIndex=None,
                   beginIndex=None):
        """
        Get matchlist for games played on given account ID and region
        and filtered using given filter parameters, if any.

        Note:

        If both beginIndex and endIndex are provided, the endIndex must be
        greater than the beginIndex. The maximum range allowed is 100,
        otherwise a Exception will be returned.

        If both beginTime and endTime are provided, the endTime must be
        greater than the beginTime. The maximum range allowed is one week,
        otherwise a Exception will be returned.

        """

        # Check api limitations over index and time.
        if beginIndex is not None and endIndex is not None:
            if beginIndex > endIndex:
                raise Exception("endIndex must be greater than beginIndex.")

            if abs(beginIndex - endIndex) > 100:
                raise Exception("The maximum index range allowed is 100.")

        if beginTime is not None and endTime is not None:
            if beginTime > endTime:
                raise Exception("endTime must be greater than beginTime.")

            if abs(beginTime - endTime) > 604800000:
                raise Exception("The maximum time range allowed is one week.")

        url = API_PATH["match_list"].format(
            region_url=self.region_url, account_id=account_id)

        # append parameters
        url += "?"
        if champion:
            url += "champion=" + str(champion) + "&"
        if queue:
            url += "queue=" + str(queue) + "&"
        if season:
            url += "season=" + str(season) + "&"
        if endTime:
            url += "endTime=" + str(endTime) + "&"
        if beginTime:
            url += "beginTime=" + str(beginTime) + "&"
        if endIndex:
            url += "endIndex=" + str(endIndex) + "&"
        if beginIndex:
            url += "beginIndex=" + str(beginIndex)

        response = requests.get(url, headers=self.headers)

        return response.json()
