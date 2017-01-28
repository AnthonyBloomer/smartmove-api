from flask_restplus import Namespace, Resource, fields
from core.connection import conn
from flask import request

api = Namespace('counties', description='Get property sale statistics for each county')

county = api.model('County', {
    'id': fields.String(required=True, description='The county identifier'),
    'county_name': fields.String(required=True, description='The county name.'),
    'average_sale_price': fields.String(description='The average sale price.'),
    'total_number_of_sales': fields.String(description="The total number of sales.")
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
class PropertyList(Resource):
    @api.doc('list_county_statistics')
    @api.marshal_list_with(county)
    def get(self):
        sort_by = 'f.id'
        sort_order = 'asc'

        if request.args.get('sort_by'):
            sort_by = 'average_sale_price' if request.args.get('sort_by') == 'price' else 'total_number_of_sales'

        if request.args.get('sort_order'):
            sort_order = 'desc' if request.args.get('sort_order') == 'desc' else 'asc'

        sql = "select * from fact_county as f " \
              "join dim_county as c on f.county_id = c.id order by %s %s" % (sort_by, sort_order)
        with conn.cursor() as cursor:
            cursor.execute(sql)
        data = cursor.fetchall()
        return data if data else api.abort(404)


@api.route('/<id>')
@api.param('id', 'The property identifier')
@api.response(404, 'Property not found')
class County(Resource):
    @api.doc('get_property')
    @api.marshal_with(county)
    def get(self, id):
        sql = "select * from fact_county as f join dim_county as c on f.county_id = c.id where f.id = %s"
        with conn.cursor() as cursor:
            cursor.execute(sql, id)
        data = cursor.fetchone()
        return data if data else api.abort(404)


@api.route('/<county_name>/<year>')
@api.param('county_name', 'The county name.')
@api.param('year', 'The year you wish to get county sale statistics for.')
@api.response(404, 'Property not found')
class GetCountyById(Resource):
    @api.doc('get_property')
    @api.marshal_with(year_stats)
    def get(self, county_name, year):
        # Get yearly sale statistics for the given county.
        sql = "select * from fact_year as f " \
              "join dim_county as d on d.id = f.county_id where county_name like %s and year = %s "
        with conn.cursor() as cursor:
            cursor.execute(sql, [county_name, year])
        y = cursor.fetchall()
        return y if y else api.abort(404)
