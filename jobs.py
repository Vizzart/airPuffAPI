
import logging.config
import os
import requests
import setting
from fuzzy.externalFuzzy import calculateExternalMandami
from fuzzy.iternalFuzzy import calculateIternalMandami
from api.esp.espService import EspService
from api.esp.endpoints import espRoute
from api.airly.endpoints import airlyRoute
from database import models
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.executors.pool import ThreadPoolExecutor, ProcessPoolExecutor


loggingConfPath = os.path.normpath(os.path.join(os.path.dirname(__file__), 'logging.conf'))
logging.config.fileConfig(loggingConfPath)
log = logging.getLogger(__name__)

host = setting.FLASK_SERVER_NAME
port = setting.FLASK_PORT

def espInsert():
    espRoute.EspInsert().post()

def ailryInsert():
    airlyRoute.AirlyInsert().post()

def setPwm():
    """

    :return:
    """
    espLastMeasurement=(models.Esp().espGetLastView())[0][0]
    frame = []
    for row in espLastMeasurement["sensorValue"]:
        if row['name'] == 'PM2.5':
            if float(row["value"]) < 25:
                frame.append(float(row["value"]))
            else:
                frame.append(25)
        elif row['name'] =='PM10':
            if float(row["value"]) < 50:
                frame.append(float(row["value"]))
            else:
                frame.append(50)
    airlyLastMeasurement = (models.Airly().airlyGetLastJsonView())[0][0]
    for row in airlyLastMeasurement["current"]["sensorValue"]:
        if row['name'] == 'PM25':
            if float(row["value"]) < 25:
                frame.append(float(row["value"]))
            else:
                frame.append(25)
        elif row['name'] =='PM10':
            if float(row["value"]) < 50:
                frame.append(float(row["value"]))
            else:
                frame.append(50)
    airlyForecastMeasurement = (models.Airly().airlyGetForecastLastJsonView())[0][0]
    for row in airlyForecastMeasurement["forecast"][0]["sensorValue"]:
        if row['name'] == 'PM25':
            if float(row["value"]) < 25:
                frame.append(float(row["value"]))
            else:
                frame.append(25)
        elif row['name'] == 'PM10':
            if float(row["value"]) < 50:
                frame.append(float(row["value"]))
            else:
                frame.append(50)
    print(frame)
    espCurrentMandami = calculateExternalMandami(frame [0],frame[1], 25, 50)
    airlyCurrentMandami = calculateExternalMandami(frame[2], frame[3], 25, 50)
    airlyForecastMandami = calculateExternalMandami(frame[4], frame[5], 25, 50)
    print(espCurrentMandami,airlyCurrentMandami, airlyForecastMandami)
    funMandami = calculateIternalMandami(airlyCurrentMandami,espCurrentMandami,airlyForecastMandami)
    print(funMandami)
    os.system("gpio mode 23 pwm ")
    set_pwm = "gpio pwm 23 " + str(funMandami)
    os.system(set_pwm)

def espReboot():
    obj = EspService()
    esp_url = f"http://{obj.host}/?cmd=reboot"
    data = {'Accept': 'application/json'}
    requests.get(esp_url,headers= data)

def schedule():

    executors = {
        'default': ThreadPoolExecutor(setting.THREAD),
        'processpool': ProcessPoolExecutor(setting.PROCESS)
    }
    job_defaults = {
        'coalesce': setting.COALESCE,
        'max_instances': setting.MAX_INSTANCES
    }
    sched = BackgroundScheduler(executors=executors, job_defaults=job_defaults)
    sched.add_job(espInsert, 'interval', seconds=setting.INTERVAL_ESP_SECONDS, id='espInsert')
    sched.add_job(ailryInsert, 'interval', seconds=setting.INTERVAL_AILRY_SECONDS, id='airlyInsert')
    sched.add_job(setPwm, 'interval', seconds=4, id='setPwm')
    sched.start()