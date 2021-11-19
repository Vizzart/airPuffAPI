# coding=utf-8
import configparser
import requests
import logging
import os
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv

log = logging.getLogger(__name__)

class EspService():

    def __init__(
            self
    ):
        self.host
        self.passwd
        self.user

    def getConfigEspFromFile(self):
        config = configparser.ConfigParser()
        config.read('./config.ini')
        self.host = config.get("esp", "host")
        # ENV
        load_dotenv()
        self.user = os.getenv("ESP_USER")
        self.passwd = os.getenv("ESP_PASSW")

    def getDataFromEsp(self):
        self.getConfigEspFromFile()
        espUrl = f"http://{self.host}/json?view=sensorupdate"
        headers = {'Accept': 'application/json'}
        response = requests.get(espUrl, headers=headers, auth=HTTPBasicAuth(self.user,self.passwd))
        return response.json(), response.status_code


    def  espReboot(self):
        self.getConfigEspFromFile()
        espUrl = f"http://{self.host}/?cmd=reboot"
        headers = {'Accept': 'application/json'}
        print(espUrl)
        response = requests.get(espUrl, headers=headers, auth= HTTPBasicAuth(self.user,self.passwd))
        return  response.status_code

