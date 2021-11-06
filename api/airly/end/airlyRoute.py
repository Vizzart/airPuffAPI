import logging

from api.airly import airlyService
from flask_restx import Resource,marshal
from api.restX import api
from api.airly.airlySerializers import  airlyJson,airlyError
from api.database import models

log = logging.getLogger(__name__)

ns = api.namespace('Airly', description='Adding new measurements to the database.')



@ns.route('/insert')
class AirlyInsert(Resource,airlyService.Airly,models.TempJson):
    """
    response[0] -json
    response[1] - json status_code
    """
    @ns.response(code=201, description='Create')
    @ns.response(code=400, description='Bad Request')
    @ns.response(code=401, description='Unauthorized')
    @ns.response(code=404, description='Not Found')
    @ns.response(code=405, description='Method Not Allowed')
    @ns.response(code=406, description='Not Acceptable')
    @ns.response(code=429, description='Too Many Requests')
    @ns.response(code=500, description='Internal Server Error')
    def post(self):
        response = super().getDataFromAirly()
        super().InsertResultJsonToDb(response, 'airly')
        print(response)
        #change status get from airly to 201
        if response[1] == 200:
            status_code = 201
            return marshal(response[0], airlyJson), status_code
        else:
            return marshal(response[0],airlyError  ), response[1]


