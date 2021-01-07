from riotwrapper.const.lor_const import REGION_URL


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
