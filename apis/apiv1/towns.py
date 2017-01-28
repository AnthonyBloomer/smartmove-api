from flask_restplus import Namespace, Resource, fields
from core.connection import conn
from flask import request
from core.utils import paginate

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
class Town(Resource):
    @api.doc('list_town_statistics')
    @api.marshal_list_with(town)
    def get(self):
        params = []
        sort_by = 'id'
        sort_order = 'asc'

        if request.args.get('sort_by'):
            sort_by = 'average_sale_price' if request.args.get('sort_by') == 'price' else 'total_number_of_sales'

        if request.args.get('sort_order'):
            sort_order = 'desc' if request.args.get('sort_order') == 'desc' else 'asc'

        sql = "select * from fact_town order by %s %s " % (sort_by, sort_order)
        sql += "limit %s, %s;"

        print sql

        for d in paginate():
            params.append(d)

        with conn.cursor() as cursor:
            cursor.execute(sql, params)
        data = cursor.fetchall()
        return data if data else api.abort(404)


@api.route('/<id>')
@api.param('id', 'The property identifier')
@api.response(404, 'Town not found')
class GetTownById(Resource):
    @api.doc('get_property')
    @api.marshal_with(town)
    def get(self, id):
        sql = "select * from fact_town where id = %s"
        with conn.cursor() as cursor:
            cursor.execute(sql, id)
        data = cursor.fetchone()
        return data if data else api.abort(404)
