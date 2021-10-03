import setting

from flask import Flask
from db_con import connection
from airly import airly


app = Flask(__name__)


def configure_app(flask_app):
    flask_app.config['FLASK_APP'] =setting.FLASK_APP
    flask_app.config['FLASK_ENV'] = setting.FLASK_ENV

def initialize_app(flask_app):
    configure_app(flask_app)
    #add blueprint

#test
#
# connection.get_api_config()
# print(airly.get_airly_results())

print (5)
if __name__ == '__main__':
    initialize_app(app)
    app.run(debug= setting.FLASK_DEBUG)
