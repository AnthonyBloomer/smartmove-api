from flask_restplus import Namespace, Resource, fields
from core.utils import paginate
from flask import request
from core.connection import conn
from urllib import unquote_plus

api = Namespace('properties', description='Property related operations')

property = api.model('Property', {
    'id': fields.String(required=True, description='The property identifier'),
    'address': fields.String(required=True, description='The address of the property.'),
    'county_name': fields.String(required=True, description='The county.'),
    'sale_type': fields.String(required=True, description="The sale type"),
    'description': fields.String(required=True, description='The description of the property.'),
    'date_time': fields.String(required=True, description='The date of sale.'),
    'price': fields.String(required=True, description='The price of the property.')
})


@api.route('/')
@api.param('offset', 'The page number.')
@api.param('sale_type', 'The sale type')
@api.response(404, 'Invalid sale type.')
class PropertyList(Resource):
    @api.doc('list_properties')
    @api.marshal_list_with(property)
    def get(self):
        params = []
        sale_type = 1
        sql = "select p.id, p.address, p.sale_type, p.date_time, p.description, p.price, c.county_name from smartmove.properties as p " \
              "left join smartmove.counties as c " \
              "on p.county_id = c.id " \
              "where p.sale_type = %s " \
              "limit %s, %s"

        if request.args.get('sale_type'):
            sale_type = int(request.args.get('sale_type'))
            if sale_type > 2:
                api.abort(404)

        params.append(sale_type)

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


@api.route('/search/<search_term>')
@api.param('search_term', 'The search query')
@api.param('sale_type', 'The sale type')
@api.response(404, 'No results found')
class Search(Resource):
    @api.doc('search')
    @api.marshal_with(property)
    def get(self, search_term):
        sale_type = 1
        params = []
        sql = "select * from smartmove.properties as p " \
              "join smartmove.counties as c " \
              "on p.county_id = c.id " \
              "where p.address like %s " \
              "and sale_type = %s "\
              "limit %s, %s"

        params.append(('%' + unquote_plus(search_term) + '%'))

        if request.args.get('sale_type'):
            sale_type = int(request.args.get('sale_type'))
            if sale_type > 2:
                api.abort(404)

        params.append(sale_type)

        for d in paginate():
            params.append(d)

        with conn.cursor() as cursor:
            cursor.execute(sql, params)
        data = cursor.fetchall()
        return data if data else api.abort(404)
