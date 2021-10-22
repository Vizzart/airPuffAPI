# coding=utf-8
import configparser
import requests

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
        self.host
        self.key = key
        self.latitude = latitude
        self.longitude = longitude
        self.distance = distance
        self.setConfigAirlyConnection()

    def setConfigAirlyConnection(self):
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
        self.setConfigAirlyConnection()
        host = self.host
        key = self.key
        latitude = self.latitude
        longitude = self.longitude
        distance = self.distance
        api_url =f"""{host}measurements/nearest?lat={latitude}&lng={longitude}&maxDistanceKM={distance}"""
        data = {'Accept': 'application/json'}
        data['apikey'] = key
        print(api_url)
        response= requests.get(api_url,headers= data)
        return response.json(), response.status_code
