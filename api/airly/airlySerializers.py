# coding=utf-8
from flask_restx import fields
from api.restX import api


airlyValue = api.inherit('airlyValues', {
   'name' : fields.String,
   'value' : fields.Float
})

airlyIndexes = api.inherit('airlyIndex', {
   'name' : fields.String,
   'value': fields.Float,
   'level': fields.String,
   'description' : fields.String,
   'advice' : fields.String,
   'color' : fields.String
})

airlyStandard = api.inherit ('airlyStandard', {
'name' : fields.String,
'pollutant' : fields.String,
'limit' : fields.Float,
'percent' : fields.Float,
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
   'current' : fields.List(fields.Nested(airlyValues,required=True)),
   'forecast': fields.List(fields.Nested(airlyValues,required=True)),
   'history' : fields.List(fields.Nested(airlyValues,required=True))

})

airlyError = api.model ('airlyError',{
   'message': fields.String
})

sensorsValue = api.model ('sensorsValue', {
    'name' : fields.String,
    'value' : fields.Float

})
current = api.model('current', {
   'fromDateTime' : fields.DateTime,
   'tillDateTime' : fields.DateTime,
   'sensorValue' : fields.Nested(sensorsValue)
})

airlyGetLastView = api.model ('airlyGetLastView', {
   'current' : fields.Nested(current)
})

airlyGetForecastLastJsonView = api.model('airlyGetForecastLastJsonView', {
   'forecast' : fields.List(fields.Nested(current))
})

airlyGetHistoryJsonLastView = api.model ('airlyGetHistoryJsonLastView', {
   'history': fields.List(fields.Nested(current))
})


