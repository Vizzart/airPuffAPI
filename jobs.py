import logging.config
import setting
from fuzzy import setPwm
from api.esp.endpoints import espRoute
from api.airly.endpoints import airlyRoute
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.executors.pool import ThreadPoolExecutor, ProcessPoolExecutor

log = logging.getLogger(__name__)

def espInsert():
    espRoute.EspInsert().post()

def ailryInsert():
    airlyRoute.AirlyInsert().post()

def fanLevel():
    setPwm.setPwm()

def espReboot():
    espRoute.EspReboot().espReboot()

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
    sched.add_job(espReboot, 'interval', minutes=setting.INTERVAL_ESP_REBOOT_MINUTES, id='espReboot')
    sched.add_job(fanLevel, 'interval', seconds=setting.INTERVAL_PWM, id='setPwm')
    sched.start()