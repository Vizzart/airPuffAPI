import logging

from api.airly import airlyService
from flask_restx import Resource,marshal
from api.restX import api
from api.airly.airlySerializers import  airlyJson,airlyError

log = logging.getLogger(__name__)

ns = api.namespace('airly', description='Get requests from Airly and insert into Database ')



@ns.route('/insert')
class AirlyResource(Resource,airlyService.Airly):
    """
    response[0] -json
    response[1] - json status_code
    """
    @ns.response(code=201, model = airlyJson, description='Create')
    @ns.response(code=400, description='Bad Request')
    @ns.response(code=401, description='Unauthorized')
    @ns.response(code=404, description='Not Found')
    @ns.response(code=405, description='Method Not Allowed')
    @ns.response(code=406, description='Not Acceptable')
    @ns.response(code=429, description='Too Many Requests')
    @ns.response(code=500, description='Internal Server Error')
    def post(self):
        response = super().getAirlyResults()
        super().airly_insert(response)
        #change status get from airly to 201
        if response[1] == 200:
            status_code = 201
            return marshal(response[0], airlyJson), status_code
        else:
            return marshal(response[0],airlyError  ), response[1]



@api.errorhandler
def handle_no_result_exception(error):
    return {'message':  str(error)}, getattr(error, 'code', 500)
