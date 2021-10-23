# coding=utf-8
from flask_restx import fields
from api.restX import api


airlyValue = api.model('values', {
   'name' : fields.String,
   'value' : fields.Float
})

airlyValues = api.model ('current', {
   'fromDateTime' : fields.Date,
   'tillDateTime' : fields.Date,
   'values' : fields.Nested(airlyValue)

})

airlyJson = api.model('Airly', {
         'current' : fields.List(fields.Nested(airlyValues,required=True))

})

airlyError = api.model ('AirlyError',{
   'message': fields.String
})
