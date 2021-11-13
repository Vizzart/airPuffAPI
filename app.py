import setting
import os
import logging.config
import jobs
from flask import Flask
from flask import Blueprint
import api.esp.espService
from api.restX import  api
from api.airly.endpoints.airlyRoute import  ns as airlyNamespace
from api.esp.endpoints.espRoute import ns as espNamespace

app = Flask(__name__)

loggingConfPath = os.path.normpath(os.path.join(os.path.dirname(__file__), 'logging.conf'))
logging.config.fileConfig(loggingConfPath)
log = logging.getLogger(__name__)

def configure_app(flaskApp):
    flaskApp.config['flaskApp'] = setting.FLASK_APP
    flaskApp.config['FLASK_SERVER_NAME'] = setting.FLASK_SERVER_NAME
    flaskApp.config['FLASK_ENV'] = setting.FLASK_ENV
    flaskApp.config['JSONIFY_PRETTYPRINT_REGULAR'] = setting.JSONIFY_PRETTYPRINT_REGULAR
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
    #api.add_namespace(rpi)
    flaskApp.register_blueprint(blueprint)



if __name__ == '__main__':
    jobs.schedule()
    initialize_app(app)
    app.run(host=setting.FLASK_SERVER_NAME ,port = setting.FLASK_PORT)
