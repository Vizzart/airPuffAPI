import traceback
import logging

from flask_restx import Api
from sqlalchemy.orm.exc import NoResultFound

import setting



api = Api(version='1.0', title='AIR PUFF API',
          description='-> ')
