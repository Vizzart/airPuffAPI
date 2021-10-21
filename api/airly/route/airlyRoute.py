import logging

from api.airly import airly
from flask_restx import Resource
from api.restX import api
from api.airly.model.airlySerializers import  airly_json,airly_error_rate

log = logging.getLogger(__name__)

ns = api.namespace('airly', description='Get requests from Airly')


airly_object = airly.Airly


@ns.route('/get')
class AirlyResource(Resource):
    @ns.response(code=200,model = airly_json, description='OK')
    @ns.response(code=400, model=airly_error_rate, description='Bad Request')
    @ns.response(code=401,model = airly_error_rate, description='Unauthorized')
    @ns.response(code=404, model=airly_error_rate, description='Not Found')
    @ns.response(code=405, model=airly_error_rate, description='Method Not Allowed')
    @ns.response(code=406, model=airly_error_rate, description='Not Acceptable')
    @ns.response(code=429, model=airly_error_rate, description='Too Many Requests')
    @ns.response(code=500, model=airly_error_rate, description='Internal Server Error')
    def get(self):
        airly_object.get_config_airly(airly_object)
        response = airly_object.get_airly_results(airly_object)
        return response[0], response[1]

#
#
@api.errorhandler
def handle_no_result_exception(error):
    return {'message':  str(error)}, getattr(error, 'code', 500)
