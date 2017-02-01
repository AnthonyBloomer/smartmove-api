from flask_restplus import Namespace, Resource
from core.connection import conn
from core.utils import paginate, gviz_json, validate_key
from flask import request

api = Namespace('charts', description='Google Charts')


@api.route('/<county_name>')
@api.param('county_name', 'The county name.')
@api.param('api_key', 'Your API key.')
@api.response(404, 'Property not found')
@api.response(401, 'Invalid API key.')
class Chart(Resource):
    def get(self, county_name):
        if request.args.get('api_key') and validate_key(request.args.get('api_key')):
            sql = 'select year, average_sale_price from fact_year as f ' \
                  'join dim_county as d ' \
                  'on d.id = f.county_id ' \
                  'join dim_property as p ' \
                  'on d.id = p.id ' \
                  'where county_name like %s'
            with conn.cursor() as cursor:
                cursor.execute(sql, county_name)
            data = cursor.fetchall()
            if not data:
                api.abort(404)
            return gviz_json(
                columns_order=("Year", "Average Sale Price"),
                order_by="Year",
                desc=[("Average Sale Price", "number"), ("Year", "String")],
                data=data
            )
        else:
            api.abort(401)


@api.route('/pie')
@api.param('api_key', 'Your API key.')
@api.response(401, 'Invalid API key.')
class Pie(Resource):
    def get(self):
        if request.args.get('api_key') and validate_key(request.args.get('api_key')):
            sql = 'select d.county_name, f.average_sale_price from fact_county as f ' \
                  'inner join dim_county as d on d.id = f.county_id'
            with conn.cursor() as cursor:
                cursor.execute(sql)
            data = cursor.fetchall()
            if not data:
                api.abort(404)
            return gviz_json(
                columns_order=("County", "Number of Sales"),
                order_by="County",
                desc=[("Number of Sales", "number"), ("County", "String")],
                data=data
            )
        else:
            api.abort(401)


@api.route('/table')
@api.param('offset', 'The page number.')
@api.param('sale_type', 'The sale type')
@api.param('api_key', 'Your API key.')
@api.response(401, 'Invalid API key.')
class Table(Resource):
    def get(self):
        if request.args.get('api_key') and validate_key(request.args.get('api_key')):
            params = []
            sql = 'select town_name, average_sale_price from fact_town limit %s, %s'
            for d in paginate():
                params.append(d)
            with conn.cursor() as cursor:
                cursor.execute(sql, params)
            data = cursor.fetchall()
            if not data:
                api.abort(404)
            return gviz_json(
                columns_order=("Town", "Average Sale Price"),
                order_by="Town",
                desc=[("Average Sale Price", "number"), ("Town", "String")],
                data=data
            )
        else:
            api.abort(401)
