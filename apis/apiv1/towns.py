# -*- coding: utf-8 -*-
from flask_restplus import Namespace, Resource, fields
from core.connection import conn
from flask import request
from core.utils import paginate, validate_key
import settings

api = Namespace('towns', description='Get property sale statistics for each town.')

town = api.model('Town', {
    'id': fields.String(required=True, description='The town identifier'),
    'town_name': fields.String(required=True, description='The town name.'),
    'average_sale_price': fields.String(description='The average sale price.'),
    'total_number_of_sales': fields.String(description="The total number of sales.")
})


@api.route('/')
@api.param('sort_by', 'The sort type.')
@api.param('sort_order', 'The sort order.')
@api.param('api_key', 'Your API key.')
@api.response(401, 'Invalid API key.')
class Town(Resource):
    @api.doc('list_town_statistics')
    @api.marshal_list_with(town)
    def get(self):
        """
        Description: Get a list of town property sale statistics.
        :return: JSON
        """
        if request.args.get('api_key') and validate_key(request.args.get('api_key')) or settings.ENV == 'TESTING':
            params = []
            sort_by = 'id'
            sort_order = 'asc'

            if request.args.get('sort_by'):
                sort_by = 'average_sale_price' if request.args.get('sort_by') == 'price' else 'total_number_of_sales'

            if request.args.get('sort_order'):
                sort_order = 'desc' if request.args.get('sort_order') == 'desc' else 'asc'

            sql = 'select id, total_number_of_sales, town_name, concat("€", format(average_sale_price, 2)) as average_sale_price ' \
                  'from fact_town ' \
                  'order by %s %s ' % (sort_by, sort_order)
            sql += "limit %s, %s;"

            for d in paginate():
                params.append(d)

            with conn.cursor() as cursor:
                cursor.execute(sql, params)
            data = cursor.fetchall()
            return data if data else api.abort(404)
        else:
            api.abort(401)


@api.route('/<id>')
@api.param('id', 'The property identifier')
@api.param('api_key', 'Your API key.')
@api.response(404, 'Town not found')
@api.response(401, 'Invalid API key.')
class GetTownById(Resource):
    @api.doc('get_town_by_id')
    @api.marshal_with(town)
    def get(self, id):
        """
        Description: Get property sale statistics for a town by its ID.
        :return: JSON
        """
        if request.args.get('api_key') and validate_key(request.args.get('api_key')) or settings.ENV == 'TESTING':
            sql = 'select id, total_number_of_sales, town_name, concat("€", format(average_sale_price, 2)) as average_sale_price ' \
                  'from fact_town ' \
                  'where id = %s'
            with conn.cursor() as cursor:
                cursor.execute(sql, id)
            data = cursor.fetchone()
            return data if data else api.abort(404)
        else:
            api.abort(401)


@api.route('/compare')
@api.param('api_key', 'Your API key.')
@api.param('town1', 'The town name.')
@api.param('town2', 'The town you want to compare the first town to.')
@api.response(401, 'Invalid API key.')
class Compare(Resource):
    @api.doc('compare_towns')
    @api.marshal_with(town)
    def get(self):
        """
        Description: Compare property sale statistics between two towns.
        :return: JSON
        """
        if request.args.get('api_key') and validate_key(request.args.get('api_key')) or settings.ENV == 'TESTING':
            sql = 'select id, total_number_of_sales, town_name, concat("€", format(average_sale_price, 2)) as average_sale_price ' \
                  'from fact_town where town_name like %s or town_name like %s'
            with conn.cursor() as cursor:
                cursor.execute(sql, [request.args.get('town1'), request.args.get('town2')])
            data = cursor.fetchall()
            if not data:
                api.abort(404)
            return data

        else:
            api.abort(401)
