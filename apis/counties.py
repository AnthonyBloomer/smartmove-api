from flask_restplus import Namespace, Resource, fields
from core.connection import conn

api = Namespace('counties', description='Get property sale statistics for each county')

county = api.model('County', {
    'id': fields.String(required=True, description='The county identifier'),
    'county_name': fields.String(required=True, description='The county.'),
    'average_sale_price': fields.String(description='The average sale price.'),
    'total_number_of_sales': fields.String(description="The total number of sales.")
})

year_stats = api.model('Year', {
    'id': fields.String(required=True, description='The county identifier'),
    'county_name': fields.String(required=True, description='The county.'),
    'average_sale_price': fields.String(description='The average sale price.'),
    'total_number_of_sales': fields.String(description="The total number of sales."),
    'year': fields.String(description="Year")
})


@api.route('/')
class PropertyList(Resource):
    @api.doc('list_county_statistics')
    @api.marshal_list_with(county)
    def get(self):
        sql = "select * from fact_county as f join dim_county as c on f.county_id = c.id"
        with conn.cursor() as cursor:
            cursor.execute(sql)
        data = cursor.fetchall()
        return data if data else api.abort(404)


@api.route('/<id>')
@api.param('id', 'The property identifier')
@api.response(404, 'Property not found')
class Property(Resource):
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
@api.param('year', 'The year.')
@api.response(404, 'Property not found')
class Property(Resource):
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
