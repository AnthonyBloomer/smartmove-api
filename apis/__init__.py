from flask_restplus import Api

from apis.apiv1.towns import api as towns
from apis.apiv1.charts import api as charts
from apis.apiv1.counties import api as counties
from apis.apiv1.countries import api as countries
from apis.apiv1.properties import api as properties

api = Api(
    title='Smartmove API',
    version='1.0',
    description='A REST API to get property sale statistics in Ireland and the UK.',
)

api.add_namespace(properties)
api.add_namespace(counties)
api.add_namespace(charts)
api.add_namespace(countries)
api.add_namespace(towns)
