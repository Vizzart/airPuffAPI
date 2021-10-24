import logging.config
import os
import requests
import setting

from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.executors.pool import ThreadPoolExecutor, ProcessPoolExecutor


loggingConfPath = os.path.normpath(os.path.join(os.path.dirname(__file__), 'logging.conf'))
logging.config.fileConfig(loggingConfPath)
log = logging.getLogger(__name__)

host = setting.FLASK_SERVER_NAME
port = setting.FLASK_PORT
def espJob():
    api_url = f'http://{host}:{port}/api/ESP/insert/new'
    requests.post(api_url)


def ailryJob():
    api_url = f'http://{host}:{port}/api/Airly/insert'
    requests.post(api_url)

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
    sched.add_job(espJob, 'interval', seconds=setting.INTERVAL_ESP_SECONDS, id='espInsert')
    sched.add_job(ailryJob, 'interval', seconds=setting.INTERVAL_AILRY_SECONDS, id='airlyInsert')
    sched.start()

