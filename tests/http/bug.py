import unittest

from pulsar.apps import http


class TestBugs(unittest.TestCase):

    def test_json(self):
        c = http.HttpClient()
        data = yield from c.get('https://api.bitfinex.com/v1/pubticker/BTCUSD')
        self.assertTrue(data)
