import logging

from api.airly import airlyService
from flask_restx import Resource,marshal
from api.restX import api
from api.airly.airlySerializers import  airlyJson,airlyError,airlyGetLastView,\
airlyGetForecastLastJsonView,airlyGetHistoryJsonLastView
from database import models

log = logging.getLogger(__name__)

ns = api.namespace('airly', description='')

@ns.route('/measurement')
class AirlyInsert(Resource, airlyService.Airly, models.TempSensorData):
    """
    response[0] -json
    response[1] - json status_code
    """
    @ns.response(code=201, description='Create')
    @ns.response(code=400, description='Bad Request')
    @ns.response(code=401, description='Unauthorized')
    @ns.response(code=404, description='Not Found')
    @ns.response(code=500, description='Internal Server Error')
    def post(self):
        response = super().getDataFromAirly()
        super().InsertResultJsonToDataBase(response, 'airly')
        if response[1] == 200:
            status_code = 201
            return marshal(response[0], airlyJson), status_code
        else:
            return marshal(response[0],airlyError ), response[1]

@ns.route('/measurement/current')
class AirlyCurrentView(Resource, models.Airly):

    @ns.response(code=200, description='OK')
    @ns.response(code=400, description='Bad Request')
    @ns.response(code=401, description='Unauthorized')
    @ns.response(code=404, description='Not Found')
    @ns.response(code=500, description='Internal Server Error')

    def get(self):
        response = super().airlyGetLastJsonView()
        return marshal(response[0][0], airlyGetLastView), response[1]

@ns.route('/measurement/forecast')
class AirlyForecastView(Resource, models.Airly):

    @ns.response(code=201, description='OK')
    @ns.response(code=400, description='Bad Request')
    @ns.response(code=401, description='Unauthorized')
    @ns.response(code=404, description='Not Found')
    @ns.response(code=500, description='Internal Server Error')

    def get(self):
        response = super().airlyGetForecastLastJsonView()
        return marshal(response[0], airlyGetForecastLastJsonView), response[1]

@ns.route('/measurement/history')
class AirlyHistoryView(Resource, models.Airly):

    @ns.response(code=200, description='OK')
    @ns.response(code=400, description='Bad Request')
    @ns.response(code=401, description='Unauthorized')
    @ns.response(code=404, description='Not Found')
    @ns.response(code=500, description='Internal Server Error')

    def get(self):
        response = super().airlyGetHistoryJsonLastView()
        return marshal(response[0], airlyGetHistoryJsonLastView), response[1]

