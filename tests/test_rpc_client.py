from pyxmr import RpcClient


def test_default_url():
    rpc_client = RpcClient()
    assert rpc_client.url == "http://127.0.0.1:18081/json_rpc"
