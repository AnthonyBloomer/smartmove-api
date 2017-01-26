from flask_restplus import Api

from .properties import api as properties
from .counties import api as counties
from .charts import api as charts
from .countries import api as countries

api = Api(
    title='Smartmove API',
    version='1.0',
    description='A REST API to get property price statistics in Ireland and the UK.',
)

api.add_namespace(properties)
api.add_namespace(counties)
api.add_namespace(charts)
api.add_namespace(countries)
