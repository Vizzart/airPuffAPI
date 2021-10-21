from flask_restx import fields
from api.restX import api

airly_json = api.model('airlyController', {
   'current' : fields.String(required= True, attribute = 'current')
})

airly_error_rate = api.model ('airlyErrorController',{
   'message': fields.String
})