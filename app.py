import setting
import os
import logging.config
from flask import Flask
from flask import Blueprint


from api.restX import  api
from api.airly.end.airlyController import  ns as airly_ns
from api.esp.end.espController import ns as esp_ns

from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.executors.pool import ThreadPoolExecutor, ProcessPoolExecutor
from api.esp.end.espController import EspResource


app = Flask(__name__)

loggingConfPath = os.path.normpath(os.path.join(os.path.dirname(__file__), 'logging.conf'))
logging.config.fileConfig(loggingConfPath)
log = logging.getLogger(__name__)

def configure_app(flask_app):
    flask_app.config['FLASK_APP'] = setting.FLASK_APP
    flask_app.config['FLASK_SERVER_NAME'] = setting.FLASK_SERVER_NAME
    flask_app.config['FLASK_ENV'] = setting.FLASK_ENV
    flask_app.config['JSONIFY_PRETTYPRINT_REGULAR'] = setting.JSONIFY_PRETTYPRINT_REGULAR
    flask_app.config['SWAGGER_UI_DOC_EXPANSION'] = setting.RESTPLUS_SWAGGER_UI_DOC_EXPANSION
    flask_app.config['RESTPLUS_VALIDATE'] = setting.RESTPLUS_VALIDATE
    flask_app.config['RESTPLUS_MASK_SWAGGER'] = setting.RESTPLUS_MASK_SWAGGER
    flask_app.config['ERROR_404_HELP'] = setting.RESTPLUS_ERROR_404_HELP

def initialize_app(flask_app):
    configure_app(flask_app)
    blueprint = Blueprint('api', __name__, url_prefix='/api')
    api.init_app(blueprint)
    api.add_namespace(airly_ns)
    api.add_namespace(esp_ns)
    #api.add_namespace(rpi)
    flask_app.register_blueprint(blueprint)

def schedule():
    executors = {
        'default': ThreadPoolExecutor(12),
        'processpool': ProcessPoolExecutor(1)
    }
    job_defaults = {
        'coalesce': True,
        'max_instances': 2
    }
    sched = BackgroundScheduler(executors=executors, job_defaults=job_defaults)
    #sched.add_job(get_airly, 'interval', minutes=15, id='ailry_insert_to_db_json')
    #sched.add_job(, 'interval', seconds =5, id='esp_insert_to_db_json')
    sched.start()


if __name__ == '__main__':
    schedule()
    initialize_app(app)
    app.run(debug=setting.FLASK_DEBUG)
