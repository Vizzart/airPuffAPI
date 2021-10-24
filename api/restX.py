from flask_restx import Api

api = Api(version='1.0', title='AIR PUFF API',
          description='-> ')

@api.errorhandler
def handle_no_result_exception(error):
    return {'message':  str(error)}
