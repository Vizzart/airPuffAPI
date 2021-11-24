import logging
import os

from flask_restx import Resource
from api.restX import api
from database import models

log = logging.getLogger(__name__)

ns = api.namespace('rpi',description ='')

@ns.route('/reboot')
class EspInsert(Resource):
    @ns.response(code=200, description='Create')
    @ns.response(code=500, description='Internal Server Error')
    def get(self):
        os.system("sudo reboot")
        return 200
