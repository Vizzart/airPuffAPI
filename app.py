import setting
import os
import logging.config
import jobs
from flask import Flask
from flask import Blueprint
import api.esp.espService
from api.restX import api
from api.airly.endpoints.airlyRoute import  ns as airlyNamespace
from api.esp.endpoints.espRoute import ns as espNamespace
from api.config.endpoints.configRoute import ns as configNamespace

app = Flask(__name__)



#logging.basicConfig(filename='log/record.log', level=logging.DEBUG, format=f'%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')


import logging.config
from pythonjsonlogger import jsonlogger
from datetime import datetime;


def configure_app(flaskApp):
    flaskApp.config['flaskApp'] = setting.FLASK_APP
    flaskApp.config['FLASK_SERVER_NAME'] = setting.FLASK_SERVER_NAME
    flaskApp.config['FLASK_ENV'] = setting.FLASK_ENV
    flaskApp.config['SWAGGER_UI_DOC_EXPANSION'] = setting.REST_SWAGGER_UI_DOC_EXPANSION
    flaskApp.config['REST_VALIDATE'] = setting.REST_VALIDATE
    flaskApp.config['RESTPLUS_MASK_SWAGGER'] = setting.REST_MASK_SWAGGER
    flaskApp.config['ERROR_404_HELP'] = setting.REST_ERROR_404_HELP



def initialize_app(flaskApp):
    configure_app(flaskApp)
    blueprint = Blueprint('api', __name__, url_prefix='/api')
    api.init_app(blueprint)
    api.add_namespace(airlyNamespace)
    api.add_namespace(espNamespace)
    api.add_namespace(configNamespace)
    flaskApp.register_blueprint(blueprint)


def main():
    #init insert
    jobs.espInsert()
    jobs.ailryInsert()
    #jobs
    jobs.schedule()
    initialize_app(app)
    app.run(host=setting.FLASK_SERVER_NAME ,port = setting.FLASK_PORT)

if __name__ == '__main__':
    main()
