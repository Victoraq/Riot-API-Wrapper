from riotwrapper.const.tft_const import (
    USER_REGION_URL
)


class TFTWrapper():

    def __init__(self, api_key, region):
        """Legends of Runeterra API Wrapper

        :param api_key: Riot Developer API Key.
        :param region: The region to execute the requests.

        """

        user_api_key = api_key

        if region in USER_REGION_URL.keys():
            self.region_url = USER_REGION_URL[region]
        else:
            raise Exception("""
                The region {} is not available.
                The currently available regions are: {}"""
                            .format(region,
                                    ', '.join(list(USER_REGION_URL.keys()))))

        self.headers = {"X-Riot-Token": user_api_key}
