# coding=utf-8
import configparser
import requests

from db_connections import  con_db

class Airly(con_db.DataBaseCon):
    def __init__(
        self,
        key,
        latitude,
        longitude,
        distance
    ):
        self.key = key
        self.latitude = latitude
        self.longitude = longitude
        self.distance = distance

    def get_config_airly(self):
        """
        """
        config = configparser.ConfigParser()
        config.read('./config.ini')
        self.key = config.get("airly", "key")
        self.latitude = config.get("airly","latitude")
        self.longitude = config.get("airly", "longitude")
        self.distance = config.get("airly", "distance")


    def get_airly_results(self):
        self.get_config_airly(self)
        key = self.key
        latitude = self.latitude
        longitude = self.longitude
        distance = self.distance
        api_url = f"https://airapi.airly.eu/v2/measurements/nearest?lat={latitude}&lng={longitude}&maxDistanceKM={distance}"
        data = {'Accept': 'application/json'}
        data['apikey'] = key
        r= requests.get(api_url,headers= data)
        return r.json()
