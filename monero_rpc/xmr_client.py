from urllib.parse import urlunparse
from uuid import uuid4
from requests_futures.sessions import FuturesSession


def parse_body(session, response):
    data = response.json()
    if "error" in data:
        raise Exception(data["error"])  # FIXME: Real error
    response.data = data["result"]


class XmrClient(object):
    def __init__(
            self,
            scheme="http",
            host="127.0.0.1",
            port=18081,
            path='/json_rpc'
    ):
        self.session = FuturesSession()  # FIXME: Set concurrency based on cpu
        self.url = urlunparse((
            scheme,
            "%s:%s" % (host, port),
            path,
            '', '', ''
        ))

    @staticmethod
    def headers():
        return {
            "content-type": "application/json",
            "user-agent": "monero-rpc/0.1"  # FIXME Read version from setup.py
        }

    def payload(self, method, params=[]):
        payload = {
            "id": str(uuid4()),
            "jsonrpc": "2.0",
            "method": method,

        }
        if len(params) > 0:
            payload["params"] = params
        return payload

    def getblockcount(self):
        return self.session.post(
            self.url,
            json=self.payload("getblockcount"),
            headers=XmrClient.headers(),
            background_callback=parse_body
        )
