
from api.airly import airly
from flask_restplus import Resource
from api.restPlus import api
from api.airly.model.airlySerializers import  airly_json,airly_error_rate

from werkzeug.exceptions import HTTPException
import json

ns = api.namespace('airly', description='Get requests from Airly')


airly_object = airly.Airly


@ns.route('/get')
class AirlyResource(Resource):
    @api.response(code = 200,model = airly_json, description='OK')
    @api.response(code=400, model=airly_error_rate, description='Bad Request')
    @api.response(code = 401,model = airly_error_rate, description='Unauthorized')
    @api.response(code=404, model=airly_error_rate, description='Not Found')
    @api.response(code=405, model=airly_error_rate, description='Method Not Allowed')
    @api.response(code=406, model=airly_error_rate, description='Not Acceptable')
    @api.response(code=429, model=airly_error_rate, description='Too Many Requests')
    @api.response(code=500, model=airly_error_rate, description='Internal Server Error')
    def get(self):
        airly_object.get_config_airly(airly_object)
        response = airly_object.get_airly_results(airly_object)
        return response[0], response[1]

