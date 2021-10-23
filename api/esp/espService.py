# coding=utf-8
import configparser
import requests
import logging
from db_connections import connectionDataBase
import json

log = logging.getLogger(__name__)

class Esp(connectionDataBase.DataBaseCon):

    def __init__(
            self,
            host
    ):
        self.host = host

    def getConfigEsp(self):
        config = configparser.ConfigParser()
        config.read('./config.ini')
        self.host = config.get("esp", "host")

    def getEspResults(self):
        self.getConfigEsp()
        host = self.host
        esp_url = f"http://{host}/json?view=sensorupdate"
        data = {'Accept': 'application/json'}
        response = requests.get(esp_url,headers= data)
        return response.json(), response.status_code

