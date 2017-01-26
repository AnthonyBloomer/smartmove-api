from flask_restplus import Namespace, Resource, fields
from flask import request
from core.utils import paginate
from core.connection import conn

api = Namespace('properties', description='Property related operations')

property = api.model('Property', {
    'id': fields.String(required=True, description='The property identifier'),
    'address': fields.String(required=True, description='The address of the property.'),
    'county_name': fields.String(required=True, description='The county.'),
    'description': fields.String(required=True, description='The description of the property.'),
    'date_time': fields.String(required=True, description='The date of sale.'),
    'price': fields.String(required=True, description='The price of the property.')
})


@api.route('/')
class PropertyList(Resource):
    @api.doc('list_properties')
    @api.marshal_list_with(property)
    def get(self):
        params = []
        sql = "select * from smartmove.properties as p " \
              "join smartmove.counties as c " \
              "on p.county_id = c.id " \
              "limit %s, %s"

        for d in paginate():
            params.append(d)
        with conn.cursor() as cursor:
            cursor.execute(sql, params)
        data = cursor.fetchall()
        return data


@api.route('/<id>')
@api.param('id', 'The property identifier')
@api.response(404, 'Property not found')
class Property(Resource):
    @api.doc('get_property')
    @api.marshal_with(property)
    def get(self, id):
        sql = "select * from smartmove.properties as p " \
              "join smartmove.counties as c " \
              "on p.county_id = c.id " \
              "where p.id = %s"
        with conn.cursor() as cursor:
            cursor.execute(sql, id)
        data = cursor.fetchone()
        return data if data else api.abort(404)
