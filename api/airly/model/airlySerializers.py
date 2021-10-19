from flask_restplus import fields
from api.restPlus import api

airly_json = api.model('airly_json', {
   'current' : fields.String(required= True, attribute = 'current')
})

airly_error_rate = api.model ('airly_json_limite',{
   'message': fields.String
})