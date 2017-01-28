import unittest
import requests


class ApiTest(unittest.TestCase):
    _base = 'http://127.0.0.1:5000/'

    def test_properties(self):
        r = requests.get(self._base + 'properties')
        self.assertTrue(r.status_code, 200)