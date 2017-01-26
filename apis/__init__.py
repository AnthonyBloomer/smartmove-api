from flask_restplus import Api

from .properties import api as ns1
from .counties import api as ns2
from .charts import api as ns3

api = Api(
    title='Smartmove API',
    version='1.0',
    description='A REST API to get property price statistics in Ireland and the UK.',
)

api.add_namespace(ns1)
api.add_namespace(ns2)
api.add_namespace(ns3)
