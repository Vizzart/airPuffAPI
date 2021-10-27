import logging.config
import os
import requests
import setting
import sys
from fuzzy import calculateMandami
from api.esp.espService import Esp
from api.airly.airlyService import Airly
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.executors.pool import ThreadPoolExecutor, ProcessPoolExecutor


loggingConfPath = os.path.normpath(os.path.join(os.path.dirname(__file__), 'logging.conf'))
logging.config.fileConfig(loggingConfPath)
log = logging.getLogger(__name__)

host = setting.FLASK_SERVER_NAME
port = setting.FLASK_PORT


def esp():
    obj = Esp(Esp.getConfigEspFromFile)
    obj.espInsertToDataBase( obj.getResultFromESP())


def ailry():
    obj = Airly(Airly.getConfigEspFromFile)
    obj.airly_insert(obj.getAirlyResults())

def pwmJob():
    obj =  Esp(Esp.getConfigEspFromFile)
    frame = obj.espGetLastFromDataBase()
    print(frame[0],frame[1])
    resultMandami = calculateMandami(frame[0],frame[1])
    print(resultMandami)
    os.system("gpio mode 23 pwm ")
    os.system("gpio pwm 23 pwm " +str(resultMandami))

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
    sched.add_job(esp, 'interval', seconds=setting.INTERVAL_ESP_SECONDS, id='espInsert')
    sched.add_job(ailry, 'interval', seconds=setting.INTERVAL_AILRY_SECONDS, id='airlyInsert')
    sched.add_job(pwmJob, 'interval', seconds=4, id='setPwm')
    sched.start()