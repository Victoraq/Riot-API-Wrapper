import requests
from riotwrapper.const.tft_const import (
    USER_REGION_URL, API_PATH, AMERICAS, EUROPE, ASIA,
    MATCH_REGION_URL, TIER_LIST, DIVISION_LIST,
    HIGH_TIER_LIST
)


class TFTWrapper():

    def __init__(self, api_key, region):
        """Legends of Runeterra API Wrapper

        :param api_key: Riot Developer API Key.
        :param region: The region to execute the requests.

        """

        user_api_key = api_key

        if region in USER_REGION_URL.keys():
            self.region = region
            self.region_url = USER_REGION_URL[region]
        else:
            raise Exception("""
                The region {} is not available.
                The currently available regions are: {}"""
                            .format(region,
                                    ', '.join(list(USER_REGION_URL.keys()))))

        self.headers = {"X-Riot-Token": user_api_key}

    def _continent_region(self, country):
        """Determine from which continent the region is.
        
        :param country: country to be determined the continent.

        """
        if country in AMERICAS:
            return MATCH_REGION_URL["AMERICAS"]
        elif country in EUROPE:
            return MATCH_REGION_URL["EUROPE"]
        elif country in ASIA:
            return MATCH_REGION_URL["ASIA"]

        return Exception("Region not available.")

    def match_by_id(self, match_id):
        """Get match by id.

        :param match_id: Match ID code.

        """

        region = self._continent_region(self.region)

        url = API_PATH["match_by_id"].format(
            region_url=region, match_id=match_id)

        response = requests.get(url, headers=self.headers)

        return response.json()

    def match_ids(self, account_id, count=None):
        """Get match id list by account id.

        :param account_id: Account ID or PUUID code.
        :param count: Number of ids.

        """

        region = self._continent_region(self.region)

        url = API_PATH["match_ids"].format(
            region_url=region, account_id=account_id)

        if count is not None:
            url += "?count=" + str(count)

        response = requests.get(url, headers=self.headers)

        return response.json()

    def league_entries(self, tier, division=None, page=None):
        """Get all the league entries.
        The entries can be devided into pages.
        If not provide the page parameter it will start at page 1.

        For the MASTER, GRANDMASTER, CHALLENGER tiers the division
        and page number are not required.

        :param tier: Tier identification name.
        :param division: Division identification number.

        The possible parameter values are:

        Tier: IRON, BRONZE, SILVER, GOLD, PLATINUM, DIAMOND,
            MASTER, GRANDMASTER, CHALLENGER

        Division: I, II, III, IV

        """

        if tier not in TIER_LIST and tier not in HIGH_TIER_LIST:
            raise Exception("""
                The tier {} is not available.
                The currently available tiers are: {}"""
                            .format(
                                    tier, 
                                    ', '.join(TIER_LIST + HIGH_TIER_LIST)
                                    ))

        if division is None and tier not in HIGH_TIER_LIST:
            raise Exception("""
                For the {} tiers the division must be provided."""
                            .format(', '.join(TIER_LIST)))

        if division not in DIVISION_LIST and division is not None:
            raise Exception("""
                The division {} is not available.
                The currently available divisions are: {}"""
                            .format(division, ', '.join(DIVISION_LIST)))

        if division == "master":
            path = API_PATH["master_entries"]
        elif division == "grandmaster":
            path = API_PATH["grandmaster_entries"]
        elif division == "challenger":
            path = API_PATH["challenger_entries"]
        else:
            path = API_PATH["master_entries"]

        url = path.format(
            region_url=self.region_url,
            tier=tier,
            division=division)

        if page:
            url += f"?page={page}"

        response = requests.get(url, headers=self.headers)

        return response.json()
