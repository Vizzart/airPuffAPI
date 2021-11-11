# coding=utf-8
import configparser
import requests
import os
import logging

from database import models
from dotenv import load_dotenv

log = logging.getLogger(__name__)

class Airly():
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

    def getConfigAirlyFromFile(self):
        """
        """
        config = configparser.ConfigParser()
        config.read('./config.ini')
        self.host = config.get("airly", "host")
        self.latitude = config.get("airly","latitude")
        self.longitude = config.get("airly", "longitude")
        self.distance = config.get("airly", "distance")

    def getDataFromAirly(self):
        #Config.ini
        self.getConfigAirlyFromFile()
        host = self.host
        latitude = self.latitude
        longitude = self.longitude
        distance = self.distance
        #ENV
        load_dotenv()
        key = os.getenv("AIRLY_KEY")
        apiUrl =f"""{host}measurements/nearest?lat={latitude}&lng=
        {longitude}&maxDistanceKM={distance}"""
        headers = {'Accept': 'application/json'}
        headers['apikey'] = key
        response= requests.get(apiUrl,headers= headers)
        return response.json(), response.status_code

