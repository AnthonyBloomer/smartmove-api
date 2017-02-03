import unittest
import requests


class ApiTest(unittest.TestCase):
    base = 'http://127.0.0.1:5000/'
    api_key = 'c0acf750-e8d3-11e6-be00-256583c415a5'

    def call(self, method):
        params = {
            'api_key': self.api_key
        }
        req = requests.get(url=self.base + method, params=params)
        return req


class PropertyTest(ApiTest):
    def test_properties(self):
        self.assertTrue(self.call('properties/').status_code, 200)

    def test_property_by_id(self):
        r = self.call('properties/6').json()
        self.assertTrue(r['county_name'], 'Dublin')

    def test_property_search(self):
        r = self.call('properties/search/ballivor')
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
