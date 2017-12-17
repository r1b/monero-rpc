from monero_rpc import XmrClient
from tests import my_vcr


@my_vcr.use_cassette()
def test_getblockcount():
    xmr_client = XmrClient()
    result = xmr_client.getblockcount().result()
    assert hasattr(result, "data")
    assert result.data["status"] == "OK"
    assert type(result.data["count"]) == int
