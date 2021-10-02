import configparser
import requests


def get_config_airly():
    """

    :return:
    """
    config = configparser.ConfigParser()
    config.read('./config.ini')
    key = config.get("airly", "key")
    latitude = config.get("airly","latitude")
    longitude = config.get("airly", "longitude")
    distance = config.get("airly", "distance")


    return key,latitude,longitude,distance

def get_airly_results(config_list = get_config_airly()):

        key = config_list[0]
        latitude = config_list[1]
        longitude = config_list[2]
        distance = config_list[3]
        api_url = f"https://airapi.airly.eu/v2/measurements/nearest?lat={latitude}&lng={longitude}&maxDistanceKM={distance}"
        data = {'Accept': 'application/json'}
        data['apikey'] = key
        r = requests.get(api_url,headers= data)
        return r.json()
