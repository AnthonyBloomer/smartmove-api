from flask_restplus import Namespace, Resource, fields
from core.connection import conn
from core.utils import validate_key
from flask import request
import settings

api = Namespace('sales', description='Get current and past property price figures.')

county = api.model('County', {
    'id': fields.String(required=True, description='The county identifier'),
    'insert_date': fields.String(description='The date property sale was recorded'),
    'county_name': fields.String(required=True, description='The county name.'),
    'average_sale_price': fields.String(description='The average sale price.'),
    'total_number_of_sales': fields.String(description="The total number of sales."),
})


@api.route('/')
@api.response(401, 'Invalid API key.')
class Property(Resource):
    @api.doc('list_properties')
    @api.marshal_list_with(county)
    def get(self):

        if request.args.get('api_key') and validate_key(request.args.get('api_key')) or settings.env == 'TESTING':

            sql = "select f.id, f.average_sale_price, f.total_number_of_sales, d.county_name, f.insert_date " \
                  "from fact_sales as f join dim_county as d on d.id = f.county_id"

            with conn.cursor() as cursor:
                cursor.execute(sql)
            data = cursor.fetchall()
            return data if data else api.abort(404)
        else:
            api.abort(401)
