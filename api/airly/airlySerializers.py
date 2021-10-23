# coding=utf-8
from flask_restx import fields
from api.restX import api


airlyValue = api.inherit('airlyValues', {
   'name' : fields.String,
   'value' : fields.Float
})

airlyIndexes = api.inherit('airlyIndex', {
   'name' : fields.String,
   'value': fields.String,
   'level': fields.String,
   'description' : fields.String,
   'advice' : fields.String,
   'color' : fields.String
})

airlyStandard = api.inherit ('airlyStandard', {
'name' : fields.String,
'pollutant' : fields.String,
'limit' : fields.String,
'percent' : fields.String,
'averaging' : fields.String
})

airlyValues = api.inherit('airlyCurrents', {
   'fromDateTime' : fields.DateTime,
   'tillDateTime' : fields.DateTime,
   'values' : fields.Nested(airlyValue),
   'indexes' : fields.List(fields.Nested(airlyIndexes)),
   'standards' :  fields.List(fields.Nested(airlyStandard))

})



airlyJson = api.model('airly', {
   'current' : fields.List(fields.Nested(airlyValues,required=True))

})

airlyError = api.model ('airlyError',{
   'message': fields.String
})

