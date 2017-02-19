from flask_restplus import Namespace, Resource, fields
from core.connection import conn
from core.utils import validate_key
from flask import request
from core.utils import paginate
import settings

api = Namespace('counties', description='Get property sale statistics for each county')

county = api.model('County', {
    'id': fields.String(required=True, description='The county identifier'),
    'county_name': fields.String(required=True, description='The county name.'),
    'average_sale_price': fields.String(description='The average sale price.'),
    'total_number_of_sales': fields.String(description="The total number of sales."),
})

year_stats = api.model('Year', {
    'id': fields.String(required=True, description='The county identifier'),
    'county_name': fields.String(required=True, description='The county name.'),
    'average_sale_price': fields.String(description='The average sale price.'),
    'total_number_of_sales': fields.String(description="The total number of sales."),
    'year': fields.String(description="Year")
})


@api.route('/')
@api.param('sort_by', 'The sort type.')
@api.param('sort_order', 'The sort order.')
@api.param('api_key', 'Your API key.')
@api.response(401, 'Invalid API key.')
class County(Resource):
    @api.doc('list_county_statistics')
    @api.marshal_list_with(county)
    def get(self):
        if request.args.get('api_key') and validate_key(request.args.get('api_key')) or settings.env == 'TESTING':
            sort_by = 'f.id'
            sort_order = 'asc'

            if request.args.get('sort_by'):
                sort_by = 'average_sale_price' if request.args.get('sort_by') == 'price' else 'total_number_of_sales'

            if request.args.get('sort_order'):
                sort_order = 'desc' if request.args.get('sort_order') == 'desc' else 'asc'
            sql = "select * from fact_county as f " \
                  "join dim_county as c on f.county_id = c.id " \
                  "order by %s %s" % (sort_by, sort_order)
            with conn.cursor() as cursor:
                cursor.execute(sql)
            data = cursor.fetchall()
            return data if data else api.abort(404)
        else:
            api.abort(401)


@api.route('/<id>')
@api.param('id', 'The property identifier')
@api.param('api_key', 'Your API key.')
@api.response(404, 'Property not found')
@api.response(401, 'Invalid API key.')
class GetCountyById(Resource):
    @api.doc('get_property')
    @api.marshal_with(county)
    def get(self, id):
        if request.args.get('api_key') and validate_key(request.args.get('api_key')) or settings.env == 'TESTING':
            sql = "select * from fact_county as f join dim_county as c on f.county_id = c.id where f.id = %s"
            with conn.cursor() as cursor:
                cursor.execute(sql, id)
            data = cursor.fetchone()
            return data if data else api.abort(404)
        else:
            api.abort(401)


@api.route('/<county_name>/<year>')
@api.param('county_name', 'The county name.')
@api.param('year', 'The year you wish to get county sale statistics for.')
@api.param('sale_type', 'The sale type.')
@api.param('api_key', 'Your API key.')
@api.response(401, 'Invalid API key.')
@api.response(404, 'Property not found')
class YearSalesForCounties(Resource):
    @api.doc('get_year_sales_for_counties')
    @api.marshal_with(year_stats)
    def get(self, county_name, year):
        if request.args.get('api_key') and validate_key(request.args.get('api_key')) or settings.env == 'TESTING':
            params = [county_name, year]
            sql = "select * from fact_year as f " \
                  "join dim_county as d on d.id = f.county_id " \
                  "where county_name like %s and year = %s limit %s, %s"

            for d in paginate():
                params.append(d)

            with conn.cursor() as cursor:
                cursor.execute(sql, params)
            y = cursor.fetchall()
            conn.close()
            return y if y else api.abort(404)
        else:
            api.abort(401)


@api.route('/compare')
@api.param('api_key', 'Your API key.')
@api.param('county1', 'The county name.')
@api.param('county2', 'The county you want to compare the first county to.')
@api.response(401, 'Invalid API key.')
class Compare(Resource):
    def get(self):
        if request.args.get('api_key') and validate_key(request.args.get('api_key')) or settings.env == 'TESTING':
            sql = 'select f.total_number_of_sales, f.average_sale_price, d.county_name from fact_county as f ' \
                  'join dim_county as d ' \
                  'on f.county_id = d.id ' \
                  'where d.county_name like %s ' \
                  'or d.county_name like %s'
            with conn.cursor() as cursor:
                cursor.execute(sql, [request.args.get('county1'), request.args.get('county2')])
            data = cursor.fetchall()
            if not data:
                api.abort(404)
            return data

        else:
            api.abort(401)
