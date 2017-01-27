from flask_restplus import Namespace, Resource
from core.connection import conn
import gviz_api
import json

api = Namespace('gcharts', description='Google charts')


@api.route('/<county_name>')
@api.param('county_name', 'The county name.')
@api.response(404, 'Property not found')
class Chart(Resource):
    def get(self, county_name):
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
        data = [tuple(d.values()) for d in data]
        data_table = gviz_api.DataTable([("Number of Sales", "number"), ("Year", "String")])
        data_table.LoadData(data)
        json_str = data_table.ToJSon(columns_order=("Year", "Number of Sales"), order_by="Year")
        parsed_json = json.loads(json_str)
        return parsed_json


@api.route('/pie')
class Pie(Resource):
    def get(self):
        sql = 'select d.county_name, f.average_sale_price from fact_county as f ' \
              'inner join dim_county as d on d.id = f.county_id'
        with conn.cursor() as cursor:
            cursor.execute(sql)
        data = cursor.fetchall()
        if not data:
            api.abort(404)
        data = [tuple(d.values()) for d in data]
        data_table = gviz_api.DataTable([("Number of Sales", "number"), ("County", "String")])
        data_table.LoadData(data)
        json_str = data_table.ToJSon(columns_order=("County", "Number of Sales"), order_by="County")
        parsed_json = json.loads(json_str)
        return parsed_json
