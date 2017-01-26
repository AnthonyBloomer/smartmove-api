from flask_restplus import Namespace, Resource, fields
from core.connection import conn

api = Namespace('towns', description='Get property sale statistics for each town.')

town = api.model('Town', {
    'id': fields.String(required=True, description='The town identifier'),
    'town_name': fields.String(required=True, description='The town name.'),
    'average_sale_price': fields.String(description='The average sale price.'),
    'total_number_of_sales': fields.String(description="The total number of sales.")
})


@api.route('/')
class PropertyList(Resource):
    @api.doc('list_town_statistics')
    @api.marshal_list_with(town)
    def get(self):
        sql = "select * from fact_town"
        with conn.cursor() as cursor:
            cursor.execute(sql)
        data = cursor.fetchall()
        return data if data else api.abort(404)


@api.route('/<id>')
@api.param('id', 'The property identifier')
@api.response(404, 'Town not found')
class Property(Resource):
    @api.doc('get_property')
    @api.marshal_with(town)
    def get(self, id):
        sql = "select * from fact_town where id = %s"
        with conn.cursor() as cursor:
            cursor.execute(sql, id)
        data = cursor.fetchone()
        return data if data else api.abort(404)
