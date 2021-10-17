# import traceback
# import logging
#
# from flask_restplus import Api
# from sqlalchemy.orm.exc import NoResultFound
#
# import setting
#
#
#
# api = Api(version='1.0', title='Air Puff API',
#           description='thesis -> air purifier api')
#
# log = logging.getLogger(__name__)
#
# @api.errorhandler
# def default_error_handler(e):
#     """
#      The @api.errorhandler decorator allows you to register a specific
#      handler for a given exception,
#      in the same manner that you can do with Flask/Blueprint @errorhandler decorator.
#     -> https://flask-restplus.readthedocs.io/en/0.9.0/errors.html
#
#     :return: message
#     """
#     message = 'An unhandled exception occurred.'
#     log.exception(message)
#
#     if not setting.FLASK_DEBUG:
#         return {'message': message}, 500
#
#
# @api.errorhandler(NoResultFound)
# def database_not_found_error_handler(e):
#     """No results found in database"""
#     log.warning(traceback.format_exc())
#     return {'message': 'A database result was required but none was found.'}, 404