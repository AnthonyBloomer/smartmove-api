from flask_restplus import Namespace, Resource
from core.connection import conn
from core.utils import gviz_json, validate_key
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
        if request.args.get('api_key') and validate_key(request.args.get('api_key')) or settings.env == 'TESTING':
            sql = 'select year, average_sale_price from fact_year as f ' \
                  'join dim_county as d ' \
                  'on d.id = f.county_id ' \
                  'where d.county_name like %s'
            with conn.cursor() as cursor:
                cursor.execute(sql, county_name)
            data = cursor.fetchall()
            if not data:
                api.abort(404)
            return gviz_json(
                desc=[("Average Sale Price", "number"), ("Year", "number")],
                data=data
            )
        else:
            api.abort(401)


@api.route('/pie')
@api.param('api_key', 'Your API key.')
@api.response(401, 'Invalid API key.')
class Pie(Resource):
    def get(self):
        if request.args.get('api_key') and validate_key(request.args.get('api_key')) or settings.env == 'TESTING':
            sql = 'select d.county_name, f.average_sale_price from fact_county as f ' \
                  'inner join dim_county as d on d.id = f.county_id'
            with conn.cursor() as cursor:
                cursor.execute(sql)
            data = cursor.fetchall()
            if not data:
                api.abort(404)
            return gviz_json(
                desc=[("County", "String"), ("Number of Sales", "number")],
                data=data
            )
        else:
            api.abort(401)


@api.route('/table')
@api.param('api_key', 'Your API key.')
@api.response(401, 'Invalid API key.')
class Table(Resource):
    def get(self):
        if request.args.get('api_key') and validate_key(request.args.get('api_key')) or settings.env == 'TESTING':
            params = []
            sql = 'select town_name, average_sale_price, total_number_of_sales from fact_town'
            with conn.cursor() as cursor:
                cursor.execute(sql, params)
            data = cursor.fetchall()
            if not data:
                api.abort(404)
            return gviz_json(
                desc=[("Town", "String"), ("Average Sale Price", "number"), ("Total Number of Sales", "number")],
                data=data
            )
        else:
            api.abort(401)


@api.route('/new-dwellings/number-of-sales')
@api.param('api_key', 'Your API key.')
@api.response(401, 'Invalid API key.')
class Table(Resource):
    def get(self):
        if request.args.get('api_key') and validate_key(request.args.get('api_key')) or settings.env == 'TESTING':
            params = []
            sql = 'select year(date_time) as Year, count(*) as Count ' \
                  'from smartmove.properties ' \
                  'where description = "New Dwelling house /Apartment" ' \
                  'group by Year '
            with conn.cursor() as cursor:
                cursor.execute(sql, params)
            data = cursor.fetchall()
            if not data:
                api.abort(404)
            return gviz_json(
                desc=[("Year", "number"), ("Count", "number")],
                data=data
            )
        else:
            api.abort(401)


@api.route('/new-dwellings/average-sale-price')
@api.param('api_key', 'Your API key.')
@api.response(401, 'Invalid API key.')
class Table(Resource):
    def get(self):
        if request.args.get('api_key') and validate_key(request.args.get('api_key')) or settings.env == 'TESTING':
            params = []
            sql = 'select year(date_time) as Year, avg(price) as Price ' \
                  'from smartmove.properties ' \
                  'where description = "New Dwelling house /Apartment" ' \
                  'group by Year'
            with conn.cursor() as cursor:
                cursor.execute(sql, params)
            data = cursor.fetchall()
            if not data:
                api.abort(404)
            return gviz_json(
                desc=[("Year", "number"), ("Price", "number")],
                data=data
            )
        else:
            api.abort(401)
