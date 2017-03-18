from flask import Blueprint
from flask_restplus import Api
from apis.apiv1.properties import api as properties
from apis.apiv1.counties import api as counties
from apis.apiv1.charts import api as charts
from apis.apiv1.countries import api as countries
from apis.apiv1.towns import api as towns

blueprint = Blueprint('api', __name__)

api = Api(
    blueprint,
    title='Smartmove API',
    version='1.0',
    description='A REST API to get property sale statistics in Ireland and the UK.',
)

api.add_namespace(properties)
api.add_namespace(counties)
api.add_namespace(charts)
api.add_namespace(countries)
api.add_namespace(towns)

