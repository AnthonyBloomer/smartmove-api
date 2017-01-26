from flask_restplus import Namespace, Resource, fields
from core.connection import conn

api = Namespace('counties', description='Get property sale statistics for each county')

county = api.model('County', {
    'county_name': fields.String(required=True, description='The county.'),
    'average_sale_price': fields.String(description='The average sale price.'),
    'total_number_of_sales': fields.String(description="The total number of sales.")
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
        return data


@api.route('/<county_name>')
@api.param('county_name', 'The county name.')
@api.response(404, 'Property not found')
class Property(Resource):
    @api.doc('get_property')
    @api.marshal_with(county)
    def get(self, county_name):
        sql = "select * from fact_county as f join dim_county as c on f.county_id = c.id where county_name like %s"
        with conn.cursor() as cursor:
            cursor.execute(sql, county_name)
        data = cursor.fetchone()
        return data if data else api.abort(404)
