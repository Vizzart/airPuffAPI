from datetime import datetime
import json
from airly import airly
from esp import esp

from sqlalchemy import create_engine
from sqlalchemy import Table,Column
from sqlalchemy.dialects.postgresql import UUID,TIMESTAMP,JSONB,INTEGER,VARCHAR
from sqlalchemy.ext.declarative import declarative_base

import configparser

import pandas as pd
# obsluga zarządzania tabelami
Base = declarative_base()

j_table = Table(
    "temp_json_status", Base.metadata
    , Column('id', INTEGER)
    , Column('uuid', UUID)
    , Column('date_current', TIMESTAMP)
    , Column('json_text', JSONB)
    , Column('api_name', VARCHAR)
    , Column('status', INTEGER)
)


def config_db():
    config = configparser.ConfigParser()
    config.read('./config.ini')
    user = config.get("db", "user")
    passwd = config.get("db","passwd")
    host = config.get("db", "host")
    port = config.get("db", "port", raw=True)
    db_name = config.get("db", "db_name")

    return user,passwd,host,port,db_name

def dbconnect(func,config_list = config_db() ):
    def wrapper(*args,**kwargs):
        user = config_list[0]
        passwd = config_list[1]
        host = config_list[2]
        port = config_list[3]
        db = config_list[4]
        engine = create_engine('postgresql://'+user+':'+passwd+'@'+host+':'+port+'/'+db)
        return func(engine)
    return wrapper

@dbconnect
def airly_insert(engine):
    json_airly = airly.get_airly_results()
    json_string = json.dumps(json_airly)
    current_date_string = str(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    api_name = 'airly'
    statment = j_table.insert().values(
        date_current=current_date_string
        , json_text=json_string
        , api_name=api_name
        , status='200'
    )
    engine.execute(statment)
    print('INSET AIRLY- TRUE ' + current_date_string)
    return json_airly

@dbconnect
def esp_insert(engine):
    json_esp = esp.get_esp_results()
    json_string = json.dumps(json_esp)
    current_date_string = str(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    api_name = 'esp'
    statment = j_table.insert().values(
        date_current = current_date_string
        ,json_text= json_string
	    ,api_name =api_name
        ,status = '200'
    )
    engine.execute(statment)
    print('INSET ESP- TRUE ' + current_date_string)
    return json_esp