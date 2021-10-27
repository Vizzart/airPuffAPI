import logging

from api.esp import espService
from flask_restx import Resource, marshal
from api.restX import api
from api.esp.espSerializers import espJson, espError


ns = api.namespace('ESP',description = 'Adding new measurements to the database.')


@ns.route('/last')
class EspGetFromDataBase(Resource,espService.Esp):
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
        response = super().espGetLastFromDataBase()
        print (response)

@ns.route('/insert/new')
class EspInsert(Resource,espService.Esp):
    """

    """
    @ns.response(code=201,model = espJson, description='Create')
    @ns.response(code=400, description='Bad Request')
    @ns.response(code=401, description='Unauthorized')
    @ns.response(code=404, description='Not Found')
    @ns.response(code=405, description='Method Not Allowed')
    @ns.response(code=406, description='Not Acceptable')
    @ns.response(code=429, description='Too Many Requests')
    @ns.response(code=500, description='Internal Server Error')

    def post(self):
        response = super().getResultFromESP()
        super().espInsertToDataBase(response)
        print(response)
        if response[1] == 200:
            status_code = 201
            return marshal(response[0], espJson), status_code
        else:
            return marshal(response[0], espError), response[1]

