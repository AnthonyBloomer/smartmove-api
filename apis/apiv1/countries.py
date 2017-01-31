from flask_restplus import Namespace, Resource, fields
from core.connection import conn
from core.utils import validate_key
from flask import request

api = Namespace('countries', description='Get country property sale statistics.')

country = api.model('Country', {
    'id': fields.String(required=True, description='The country identifier'),
    'country_name': fields.String(required=True, description='The county name.'),
    'average_sale_price': fields.String(description='The average sale price.'),
    'total_number_of_sales': fields.String(description="The total number of sales.")
})


@api.route('/')
@api.param('api_key', 'Your API key.')
@api.response(401, 'Invalid API key.')
class Country(Resource):
    @api.doc('list_country_statistics')
    @api.marshal_list_with(country)
    def get(self):
        if request.args.get('api_key') and validate_key(request.args.get('api_key')):
            sql = "select * from fact_country as f join dim_country as c on f.country_id = c.id"
            with conn.cursor() as cursor:
                cursor.execute(sql)
            data = cursor.fetchall()
            return data if data else api.abort(404)
        else:
            api.abort(401)


@api.route('/<id>')
@api.param('id', 'The country identifier')
@api.param('api_key', 'Your API key.')
@api.response(404, 'Property not found')
@api.response(401, 'Invalid API key.')
class GetCountyById(Resource):
    @api.doc('get_country_by_id')
    @api.marshal_with(country)
    def get(self, id):
        if request.args.get('api_key') and validate_key(request.args.get('api_key')):
            sql = "select * from fact_country as f join dim_country as c on f.country_id = c.id where f.id = %s"
            with conn.cursor() as cursor:
                cursor.execute(sql, id)
            data = cursor.fetchone()
            return data if data else api.abort(404)
        else:
            api.abort(401)