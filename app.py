import setting
import json

from flask import Flask
from flask import Blueprint

from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.executors.pool import ThreadPoolExecutor, ProcessPoolExecutor

from api.airly import airly
from api.esp import esp
from api.restPlus import  api
from api.airly.route.airlyRoute import  ns as airly_ns

app = Flask(__name__)
# dodać Logger

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
    #api.add_namespace(esp)
    #api.add_namespace(rpi)
    flask_app.register_blueprint(blueprint)
#
# @app.route('/airly/insert', methods= ['GET', 'POST'])
# def get_airly():
#     a = airly.Airly
#     r = a.airly_insert(a, a.get_airly_results(a))
#     return r
#
# @app.route('/esp/insert' , methods= ['GET', 'POST'])
# def get_esp():
#     e = esp.Esp
#     r = e.esp_insert(e,e.get_esp_results(e))
#     return r

def schedule ():
    executors = {
        'default': ThreadPoolExecutor(12),
        'processpool': ProcessPoolExecutor(1)
    }
    job_defaults = {
        'coalesce': True,
        'max_instances': 2
    }
    sched = BackgroundScheduler(executors=executors, job_defaults=job_defaults)
    sched.add_job(get_airly, 'interval', minutes=15, id='ailry_insert_to_db_json')
    sched.add_job(get_esp, 'interval', seconds =5, id='esp_insert_to_db_json')
    sched.start()


if __name__ == '__main__':
    #schedule()
    initialize_app(app)
    app.run(debug=setting.FLASK_DEBUG)
