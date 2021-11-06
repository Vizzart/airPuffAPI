# coding=utf-8
import configparser
import requests
import logging
from api.database import models
from sqlalchemy.orm import Session

log = logging.getLogger(__name__)

class EspService():

    def __init__(
            self,
            host
    ):
        self.host = host

    def getConfigEspFromFile(self):
        """
        getting host from config.ini file
        :return:
        """
        config = configparser.ConfigParser()
        config.read('./config.ini')
        self.host = config.get("esp", "host")

    def getDataFromEsp(self):
        self.getConfigEspFromFile()
        host = self.host
        espUrl = f"http://{host}/json?view=sensorupdate"
        headers = {'Accept': 'application/json'}
        response = requests.get(espUrl,headers= headers)
        print(response)
        return response.json(), response.status_code

