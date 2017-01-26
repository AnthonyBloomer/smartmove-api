from flask_restplus import Api

from .v1 import api as ns1

api = Api(
    title='Smartmove API',
    version='1.0',
    description='A REST API to get property price statistics in Ireland and the UK.',
)

api.add_namespace(ns1)
