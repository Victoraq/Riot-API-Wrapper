from riotwrapper.lor import LoRWrapper
from riotwrapper.const.lor_const import REGION_URL
import pytest


class TestLoRWrapper:

    def test_wrong_region(self):
        """Tests the exception raised after try to initialize
        the wrapper with a not available region"""

        region = "WRONG"

        with pytest.raises(Exception) as region_info:
            _ = LoRWrapper("key", region=region)

        assert f"{region} is not available" in str(region_info.value)
        assert ', '.join(list(REGION_URL.keys())) in str(region_info.value)
