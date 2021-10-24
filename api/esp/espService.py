# coding=utf-8
import configparser
import requests
import logging
from db_connections import connectionDataBase

from datetime import datetime
from sqlalchemy.orm import Session

import json

log = logging.getLogger(__name__)

class Esp(connectionDataBase.DataBaseCon):

    def __init__(
            self,
            host
    ):
        self.host = host

    def getConfigEspFromFile(self):
        config = configparser.ConfigParser()
        config.read('./config.ini')
        self.host = config.get("esp", "host")

    def getResultFromESP(self):
        self.getConfigEspFromFile()
        host = self.host
        esp_url = f"http://{host}/json?view=sensorupdate"
        data = {'Accept': 'application/json'}
        response = requests.get(esp_url,headers= data)
        print(response)
        return response.json(), response.status_code

    def espInsertToDataBase(self, espResponse):
        engine = self.dbconnect()
        #self.engine = engine
        json_string = json.dumps(espResponse[0])
        current_date_string = str(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        api_name = 'esp'
        with Session(engine) as session:
            statement = self.j_table.insert().values(
                date_current=current_date_string,
                json_text=json_string,
                api_name=api_name,
                status=espResponse[1]
            )
            session.execute(statement)
            session.commit()
            session.close()
        # print('ESP ->' +f'{espResponse[0]}' + f'status code:{espResponse[1]} -> current date : ' + current_date_string)
    def espGetLastFromDataBase(self):
        engine = self.dbconnect()
        with Session(engine) as session:
            sql = ('select * from esp order by date_current desc')
            statement = sql
