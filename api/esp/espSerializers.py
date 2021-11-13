
from flask_restx import fields
from api.restX import api

espValue = api.model ('espValue', {
    'ValueNumber' : fields.Integer,
    'Name' : fields.String,
    'Value': fields.Float
})


espTaskValues = api.model ('espTaskValues', {
    'TaskValues' : fields.List(fields.Nested(espValue))
})


espJson = api.model('espSensors', {
    'Sensors' : fields.List(fields.Nested(espTaskValues))
})

espError = api.model ('espError',{
    'message': fields.String
})


sensorsValue = api.model ('sensorsValue', {
    'name' : fields.String,
    'value' : fields.Float

})
espGetLastView = api.model ('espGetLastView', {
    'sensorValue' : fields.Nested(sensorsValue)

})

