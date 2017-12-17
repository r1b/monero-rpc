from monero_rpc import XmrClient


def test_url_parse():
    xmr_client = XmrClient()
    assert xmr_client.url == "http://127.0.0.1:18081/json_rpc"
