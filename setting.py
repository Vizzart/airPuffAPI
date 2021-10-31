#Flask settings
FLASK_APP = 'app.py'
FLASK_SERVER_NAME = 'localhost'
FLASK_PORT= 5000
FLASK_DEBUG = True
FLASK_ENV = 'development'
JSONIFY_PRETTYPRINT_REGULAR = True
#Flask-Restplus settings
RESTPLUS_SWAGGER_UI_DOC_EXPANSION = 'list'
RESTPLUS_VALIDATE = True
RESTPLUS_MASK_SWAGGER =False
RESTPLUS_ERROR_404_HELP = False
#JOBS
THREAD = 12
PROCESS = 1
MAX_INSTANCES = 5
INTERVAL_ESP_SECONDS = 5
INTERVAL_AILRY_SECONDS = 20
COALESCE = True
