import unittest
import requests


class ApiTest(unittest.TestCase):
    base = 'http://0.0.0.0:33507/'

    def call(self, method):
        req = requests.get(url=self.base + method)
        return req


class PropertyTest(ApiTest):
    def test_properties(self):
        self.assertTrue(self.call('properties/').status_code, 200)

    def test_property_by_id(self):
        r = self.call('properties/6').json()
        self.assertTrue(r['county_name'], 'Dublin')

    def test_property_search(self):
        r = self.call('properties/search/ballivor/')
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


class ChartTest(ApiTest):
    def test_avg_county(self):
        req = self.call('charts/dublin')
        self.assertTrue(req.status_code, 200)

    def test_pie_chart(self):
        req = self.call('charts/counties/average-sale-price')
        self.assertTrue(req.status_code, 200)

    def test_town_table(self):
        req = self.call('charts/table')
        self.assertTrue(req.status_code, 200)

    def test_avg_dwellings(self):
        req = self.call('new-dwellings/average-sale-price')
        self.assertTrue(req.status_code, 200)

    def test_sum_dwellings(self):
        req = self.call('new-dwellings/number-of-sales')
        self.assertTrue(req.status_code, 200)
