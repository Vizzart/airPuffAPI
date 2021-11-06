import atexit
import logging.config
import os
import requests
import setting
import sys
from fuzzy import calculateMandami
from api.esp.espService import EspService
from api.esp.end import espRoute
from api.airly.end import airlyRoute
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.executors.pool import ThreadPoolExecutor, ProcessPoolExecutor



loggingConfPath = os.path.normpath(os.path.join(os.path.dirname(__file__), 'logging.conf'))
logging.config.fileConfig(loggingConfPath)
log = logging.getLogger(__name__)

host = setting.FLASK_SERVER_NAME
port = setting.FLASK_PORT




def espInsert():
#     response = EspService(EspService.getConfigEspFromFile)
#     print(response.getDataFromEsp())
#     temp = TempJson
#     temp.createEngine(temp)
#     temp.InsertResultJsonToDb(temp,response.getDataFromEsp(),'esp')
    espRoute.EspInsert().post()

def ailryInsert():
    airlyRoute.AirlyInsert().post()

def setPwm():

    obj =  EspService(EspService.getConfigEspFromFile)
    frame = obj.espGetLastFromDataBase()
    print(frame[0],frame[1])
    if (frame[0] != 0) and (frame[1] !=0):
        resultMandami = calculateMandami(frame[0],frame[1])
    print(resultMandami)
    os.system("gpio mode 23 pwm ")
    set_pwm = "gpio pwm 23 " + str(resultMandami)
    os.system(set_pwm)

def espReboot():
    obj = EspService
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