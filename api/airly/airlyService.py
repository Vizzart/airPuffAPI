# coding=utf-8

import configparser
import json
import requests
from datetime import datetime
from sqlalchemy.orm import Session

from db_connections import  connectionDataBase

class Airly(connectionDataBase.DataBaseCon):
    def __init__(
        self,
        host,
        key,
        latitude,
        longitude,
        distance
    ):
        self.host = host
        self.key = key
        self.latitude = latitude
        self.longitude = longitude
        self.distance = distance

    def getConfigEspFromFile(self):
        """
        """
        config = configparser.ConfigParser()
        config.read('./config.ini')
        self.host = config.get("airly", "host")
        self.key = config.get("airly", "key")
        self.latitude = config.get("airly","latitude")
        self.longitude = config.get("airly", "longitude")
        self.distance = config.get("airly", "distance")

    def getAirlyResults(self):
        self.getConfigEspFromFile()
        host = self.host
        key = self.key
        latitude = self.latitude
        longitude = self.longitude
        distance = self.distance
        api_url =f"""{host}measurements/nearest?lat={latitude}&lng={longitude}&maxDistanceKM={distance}"""
        data = {'Accept': 'application/json'}
        data['apikey'] = key
        response= requests.get(api_url,headers= data)
        return response.json(), response.status_code

    def airly_insert(self, airlyResponse):
        engine = self.dbconnect()
        json_string = json.dumps(airlyResponse[0])
        current_date_string = str(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        api_name = 'airly'
        # self.dbconnect(self)
        with Session(engine) as session:
            statement = self.j_table.insert().values(
                date_current=current_date_string,
                json_text=json_string,
                api_name=api_name,
                status=airlyResponse[1]
            )
            session.execute(statement)
            session.commit()
            session.close()