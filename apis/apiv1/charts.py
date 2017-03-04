from flask_restplus import Namespace, Resource
from core.connection import conn
from core.utils import gviz_json, validate_key, paginate
from flask import request
import settings

api = Namespace('charts', description='Get JSON data that can easily be consumed by the Google Charts API.')


@api.route('/<county_name>')
@api.param('county_name', 'The county name.')
@api.param('api_key', 'Your API key.')
@api.response(404, 'Property not found')
@api.response(401, 'Invalid API key.')
class Chart(Resource):
    def get(self, county_name):
        """
        Description: Get average sale price for each year for the given county.
        :return: JSON
        """
        if request.args.get('api_key') and validate_key(request.args.get('api_key')) or settings.env == 'TESTING':
            sql = 'select average_sale_price as Price, year as Year from fact_year as f ' \
                  'join dim_county as d ' \
                  'on d.id = f.county_id ' \
                  'where d.county_name like %s'
            with conn.cursor() as cursor:
                cursor.execute(sql, county_name)
            data = cursor.fetchall()
            if not data:
                api.abort(404)
            return gviz_json(
                desc=[("Price", "number"), ("Year", "number")],
                columns_order=("Year", "Price"),
                data=data
            )
        else:
            api.abort(401)


@api.route('/counties/average-sale-price')
@api.param('api_key', 'Your API key.')
@api.param('per_page', 'The number of results we will show. Default is 10.')
@api.response(401, 'Invalid API key.')
class Pie(Resource):
    def get(self):
        """
        Description: Get average sale price for each county.
        :return: JSON
        """
        if request.args.get('api_key') and validate_key(request.args.get('api_key')) or settings.env == 'TESTING':
            per_page = 10
            if request.args.get('per_page'):
                per_page = request.args.get('per_page')
            params = []
            sql = 'select d.county_name as County, f.average_sale_price as Price from fact_county as f ' \
                  'inner join dim_county as d on d.id = f.county_id order by Price desc limit %s, %s'
            for d in paginate(per_page=per_page):
                params.append(d)
            with conn.cursor() as cursor:
                cursor.execute(sql, params)
            data = cursor.fetchall()
            if not data:
                api.abort(404)
            return gviz_json(
                desc=[("County", "String"), ("Price", "number")],
                data=data
            )
        else:
            api.abort(401)


@api.route('/table')
@api.param('api_key', 'Your API key.')
@api.param('page', 'The page number.')
@api.response(401, 'Invalid API key.')
class Table(Resource):
    def get(self):
        """
        Description: Get average sale price and number of sales for each town.
        :return: JSON
        """
        if request.args.get('api_key') and validate_key(request.args.get('api_key')) or settings.env == 'TESTING':
            params = []
            sql = 'select town_name as Town, total_number_of_sales as Count, average_sale_price as Price ' \
                  'from fact_town limit %s, %s'
            for d in paginate():
                params.append(d)
            with conn.cursor() as cursor:
                cursor.execute(sql, params)

            data = cursor.fetchall()
            if not data:
                api.abort(404)
            return gviz_json(
                data=data,
                desc=[("Town", "String"), ("Count", "number"), ("Price", "number")],
                columns_order=("Town", "Count", "Price"),
            )
        else:
            api.abort(401)


@api.route('/new-dwellings/number-of-sales')
@api.param('api_key', 'Your API key.')
@api.response(401, 'Invalid API key.')
class DwellingNumOfSales(Resource):
    def get(self):
        """
        Description: Get number of sales of new dwellings between 2010-2016
        :return: JSON
        """
        if request.args.get('api_key') and validate_key(request.args.get('api_key')) or settings.env == 'TESTING':
            params = []
            sql = 'select year(date_time) as Year, count(*) as Count ' \
                  'from smartmove.properties ' \
                  'where description = "New Dwelling house /Apartment" ' \
                  'and year(date_time) != 2017 ' \
                  'group by Year '
            with conn.cursor() as cursor:
                cursor.execute(sql, params)
            data = cursor.fetchall()
            if not data:
                api.abort(404)
            return gviz_json(
                desc=[("Year", "number"), ("Count", "number")],
                columns_order=("Count", "Year"),
                data=data
            )
        else:
            api.abort(401)


@api.route('/new-dwellings/average-sale-price')
@api.param('api_key', 'Your API key.')
@api.response(401, 'Invalid API key.')
class DwellingAverageSalePrice(Resource):
    def get(self):
        """
        Description: Get average sale price of new dwellings between 2010-2016
        :return: JSON
        """
        if request.args.get('api_key') and validate_key(request.args.get('api_key')) or settings.env == 'TESTING':
            params = []
            sql = 'select year(date_time) as Year, avg(price) as Price ' \
                  'from smartmove.properties ' \
                  'where description = "New Dwelling house /Apartment" ' \
                  'and year(date_time) != 2017 ' \
                  'group by Year'
            with conn.cursor() as cursor:
                cursor.execute(sql, params)
            data = cursor.fetchall()
            if not data:
                api.abort(404)
            return gviz_json(
                desc=[("Year", "number"), ("Price", "number")],
                columns_order=("Price", "Year"),
                data=data
            )
        else:
            api.abort(401)
