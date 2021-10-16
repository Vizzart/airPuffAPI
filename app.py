import setting

from airly import airly
from esp import esp
from flask import Flask
from apscheduler.schedulers.background import BackgroundScheduler

app = Flask(__name__)


def configure_app(flask_app):
    flask_app.config['FLASK_APP'] = setting.FLASK_APP
    flask_app.config['FLASK_SERVER_NAME'] = setting.FLASK_SERVER_NAME
    flask_app.config['FLASK_ENV'] = setting.FLASK_ENV

def initialize_app(flask_app):
    configure_app(flask_app)
    #add blueprint
@app.route('/airly/insert')
def get_airly():
    a = airly.Airly
    r = a.airly_insert(a, a.get_airly_results(a))
    return r

@app.route('/esp/insert')
def get_esp():
    e = esp.Esp
    r = e.esp_insert(e,e.get_esp_results(e))
    return r

def schedule ():
    sched = BackgroundScheduler()
    sched.add_job(get_airly, 'interval', minutes=15, id='ailry_insert_to_db_json')
    sched.add_job(get_esp, 'interval', seconds=15, id='esp_insert_to_db_json')
    sched.start()


if __name__ == '__main__':
    schedule()
    initialize_app(app)
    app.run(debug= setting.FLASK_DEBUG)
