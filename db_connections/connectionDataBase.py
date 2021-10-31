# coding=utf-8
import configparser
import json
import logging
from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy import Table, Column
from sqlalchemy.dialects.postgresql import UUID, TIMESTAMP, JSONB, INTEGER, VARCHAR, NUMERIC
from sqlalchemy.ext.declarative import declarative_base


log = logging.getLogger(__name__)



class DataBaseCon(object):
    base = declarative_base()
    j_table = Table(
        "temp_json_status", base.metadata
        , Column('id', INTEGER)
        , Column('uuid', UUID)
        , Column('date_current', TIMESTAMP)
        , Column('json_text', JSONB)
        , Column('api_name', VARCHAR)
        , Column('status', INTEGER)
    )
    esp_table = Table(
        "esp_sensor", base.metadata
        , Column('id', INTEGER)
        , Column('uuid', UUID)
        , Column('date_current', TIMESTAMP)
        , Column('pm_10', NUMERIC)
        , Column('pm_2_5', NUMERIC)
    )

    def __init__(self):
        self.engine


    def config_db(self):
        config = configparser.ConfigParser()
        config.read('./config.ini')
        user = config.get("db", "user")
        passwd = config.get("db", "passwd")
        host = config.get("db", "host")
        port = config.get("db", "port", raw=True)
        db_name = config.get("db", "db_name")
        return user, passwd, host, port, db_name

    def dbconnect(self):
        config_list = self.config_db()
        user = config_list[0]  # self.user
        passwd = config_list[1]  # self.passwd
        host = config_list[2]  # self.host
        port = config_list[3]  # self.port
        db = config_list[4]  # self.db_name
        engine = create_engine(
            'postgresql://' + user + ':' + passwd + '@' + host + ':' + port + '/' + db
        )
        return engine


        #print('INSET AIRLY'  +f'{airlyResponse[0]}' f'status code:{airlyResponse[1]} -> current date :' + current_date_string)
    #
    # def espInsert(self, espResponse):
    #     engine = self.dbconnect()
    #     self.engine = engine
    #     json_string = json.dumps(espResponse[0])
    #     current_date_string = str(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    #     api_name = 'esp'
    #     with Session(engine) as session:
    #         statement = self.j_table.insert().values(
    #             date_current=current_date_string,
    #             json_text=json_string,
    #             api_name=api_name,
    #             status=espResponse[1]
    #         )
    #         session.execute(statement)
    #         session.commit()
    #         session.close()
    #     #print('ESP ->' +f'{espResponse[0]}' + f'status code:{espResponse[1]} -> current date : ' + current_date_string)
    #
