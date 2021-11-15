import logging

from api.esp import espService
from flask_restx import Resource, marshal
from api.restX import api
from api.esp.espSerializers import espJson, espError,espGetLastView
from database import models

log = logging.getLogger(__name__)

ns = api.namespace('esp',description ='')

@ns.route('/current')
class EspGetFromDataBase(Resource, models.Esp):
    """

    """
    @ns.response(code=201, description='Create')
    @ns.response(code=400, description='Bad Request')
    @ns.response(code=401, description='Unauthorized')
    @ns.response(code=404, description='Not Found')
    @ns.response(code=405, description='Method Not Allowed')
    @ns.response(code=406, description='Not Acceptable')
    @ns.response(code=429, description='Too Many Requests')
    @ns.response(code=500, description='Internal Server Error')

    def get(self):
        response = super().espGetLastView()
        return marshal(response[0][0], espGetLastView), response[1]

@ns.route('/insert')
class EspInsert(Resource, espService.EspService, models.TempSensorData):
    """

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
        response = super().getDataFromEsp()
        super().InsertResultJsonToDataBase(response, 'esp')
        if response[1] == 200:
            status_code = 201
            return marshal(response[0], espJson), status_code
        else:
            return marshal(response[0], espError), response[1]

