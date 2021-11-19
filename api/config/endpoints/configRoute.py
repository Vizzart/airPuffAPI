import logging

from flask_restx import Resource, marshal
from api.restX import api
from database import models

log = logging.getLogger(__name__)

ns = api.namespace('config',description ='')

@ns.route('/norms')
class EspInsert(Resource, models.Norms):
    """

    """
    @ns.response(code=201, description='Create')
    @ns.response(code=400, description='Bad Request')
    @ns.response(code=401, description='Unauthorized')
    @ns.response(code=404, description='Not Found')
    @ns.response(code=500, description='Internal Server Error')

    def get(self):
        response = super().getConfigNorms()
        print(response)
        # if response[1] == 200:
        #     status_code = 201
        #     return marshal(response[0], espJson), status_code
        # else:
        #     return marshal(response[0], espError), response[1]
