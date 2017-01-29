import unittest
import requests


class ApiTest(unittest.TestCase):
    _base = 'http://127.0.0.1:5000/'

    def call(self, method, params=None):
        return requests.get(url=self._base + method, params=params)


class PropertyTest(ApiTest):
    def test_properties(self):
        self.assertTrue(self.call('properties').status_code, 200)

    def test_property_by_id(self):
        r = self.call('properties/6').json()
        self.assertTrue(r['county_name'], 'Dublin')

    def test_property_search(self):
        r = self.call('properties/search/ballivor')
        print r.json()
        self.assertTrue(r.status_code, 200)


class TownTest(ApiTest):
    def test_towns(self):
        self.assertTrue(self.call('towns').status_code, 200)

    def test_town_by_id(self):
        r = self.call('towns/3').json()
        self.assertTrue(r['town_name'], 'Adare')


class CountyTest(ApiTest):
    def test_counties(self):
        self.assertTrue(self.call('counties').status_code, 200)

    def test_county_by_id(self):
        r = self.call('counties/3').json()
        self.assertTrue(r['county_name'], 'Clare')


class CountryTest(ApiTest):
    def test_countries(self):
        self.assertTrue(self.call('countries').status_code, 200)

    def test_country_by_id(self):
        r = self.call('countries/1').json()
        self.assertTrue(r['country_name'], 'Ireland')