import setting
import os
import logging.config
from flask import Flask
from flask import Blueprint
import api.esp.espService

from api.restX import  api
from api.airly.end.airlyController import  ns as airly_ns
from api.esp.end.espController import ns as esp_ns

app = Flask(__name__)

loggingConfPath = os.path.normpath(os.path.join(os.path.dirname(__file__), 'logging.conf'))
logging.config.fileConfig(loggingConfPath)
log = logging.getLogger(__name__)



def configure_app(flaskApp):
    flaskApp.config['flaskApp'] = setting.FLASK_APP
    flaskApp.config['FLASK_SERVER_NAME'] = setting.FLASK_SERVER_NAME
    flaskApp.config['FLASK_ENV'] = setting.FLASK_ENV
    flaskApp.config['JSONIFY_PRETTYPRINT_REGULAR'] = setting.JSONIFY_PRETTYPRINT_REGULAR
    flaskApp.config['SWAGGER_UI_DOC_EXPANSION'] = setting.RESTPLUS_SWAGGER_UI_DOC_EXPANSION
    flaskApp.config['RESTPLUS_VALIDATE'] = setting.RESTPLUS_VALIDATE
    flaskApp.config['RESTPLUS_MASK_SWAGGER'] = setting.RESTPLUS_MASK_SWAGGER
    flaskApp.config['ERROR_404_HELP'] = setting.RESTPLUS_ERROR_404_HELP

def initialize_app(flaskApp):
    configure_app(flaskApp)
    blueprint = Blueprint('api', __name__, url_prefix='/api')
    api.init_app(blueprint)
    api.add_namespace(airly_ns)
    api.add_namespace(esp_ns)
    #api.add_namespace(rpi)
    flaskApp.register_blueprint(blueprint)




if __name__ == '__main__':
    from jobs import schedule
    #schedule()
    initialize_app(app)
    app.run(host=setting.FLASK_SERVER_NAME ,port = setting.FLASK_PORT)
