import unittest
import requests


class ApiTest(unittest.TestCase):
    _base = 'http://127.0.0.1:5000/'

    def call(self, method, params=None):
        return requests.get(self._base + method)


class PropertyTest(ApiTest):
    def test_properties(self):
        self.assertTrue(self.call('properties').status_code, 200)

    def test_property_by_id(self):
        r = self.call('properties/6').json()
        self.assertTrue(r['county_name'], 'Dublin')


class TownTest(ApiTest):
    def test_towns(self):
        self.assertTrue(self.call('towns').status_code, 200)


class CountyTest(ApiTest):
    def test_counties(self):
        self.assertTrue(self.call('counties').status_code, 200)


class CountryTest(ApiTest):
    def test_countries(self):
        self.assertTrue(self.call('countries').status_code, 200)
