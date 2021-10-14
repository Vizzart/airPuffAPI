import setting


from db_con import connection

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

@app.route('/airly/insert', methods = ['POST','GET'])
def get_airly():
    r =  connection.airly_insert()
    return r

@app.route('/esp/insert', methods = ['POST','GET'])
def get_esp():
    r = connection.esp_insert()
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
