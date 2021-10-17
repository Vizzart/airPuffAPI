# coding=utf-8
import configparser
import requests

from db_connections import con_db


class Esp(con_db.DataBaseCon):

    def __init__(self,host):
        self.host = host

    def get_config_esp(self):
        config = configparser.ConfigParser()
        config.read('./config.ini')
        self.host = config.get("esp", "host")

    def get_esp_results(self):
        self.get_config_esp(self)
        host = self.host
        try:
            esp_url = f"http://{host}/json?view=sensorupdate"
            r = requests.get(esp_url)
            return r.json(), r.status_code
        except requests.exceptions.ConnectionError:
            return "Connection refused", r.status_code
