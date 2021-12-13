from flask_restx import Api
from .cagnotte import ns as cagnotte_ns


api = Api(
    title='My overpowered API',
    version='0.1',
    description='Cagnoting',
)

api.add_namespace(cagnotte_ns, path='/api')
cagnotte_ns.load()
