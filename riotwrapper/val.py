from riotwrapper.const.val_const import (
    REGION_URL, API_PATH
)
import requests


class ValWrapper():

    def __init__(self, api_key, region):
        """Valorant API Wrapper

        :param api_key: Riot Developer API Key.
        :param region: The region to execute the requests.

        """

        user_api_key = api_key

        if region in REGION_URL.keys():
            self.region = region
            self.region_url = REGION_URL[region]
        else:
            raise Exception("""
                The region {} is not available.
                The currently available regions are: {}"""
                            .format(region,
                                    ', '.join(list(REGION_URL.keys()))))

        self.headers = {"X-Riot-Token": user_api_key}

    def platform_data(self):
        """Get VALORANT status for the given platform."""

        url = API_PATH["platform_data"].format(region_url=self.region_url)

        response = requests.get(url, headers=self.headers)

        return response.json()

    def contents(self, locale=None):
        """Get content optionally filtered by locale.
        
        :param locale: Locale identification string.
            Consult the API docs for the locale list.

        """

        url = API_PATH["contents"].format(region_url=self.region_url)

        if locale is not None:
            url += "?locale=" + locale

        response = requests.get(url, headers=self.headers)

        return response.json()
