import configparser
import requests


def get_config_esp():

    config = configparser.ConfigParser()
    config.read('./config.ini')
    host = config.get("esp", "host")
    return host

def get_esp_results(host =get_config_esp() ):
    try:
        esp_url = f"http://{host}/json?view=sensorupdate"
        r =  requests.get(esp_url)
        print(r.status_code)
        return r.json(), r.status_code

    except requests.exceptions.ConnectionError:
        return  "Connection refused"