
from flask_restx import fields
from api.restX import api

espTaskValues = api.model ('Value', {
    'ValueNumber' : fields.Integer,
    'Name' : fields.String,
    'Value': fields.String
})


espLoop = api.model ('TaskValues', {
    'TaskValues' : fields.List(fields.Nested(espTaskValues))
})


espJson = api.model('Sensors', {
         'Sensors' : fields.List(fields.Nested(espLoop))#fields.List(fields.Nested(espLoop,required=True))

})

espError = api.model ('EspError',{
   'message': fields.String
})
