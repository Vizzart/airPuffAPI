# coding=utf-8
import logging
import json
from datetime import datetime

from api.database.connectionDb import connectionDb
from sqlalchemy import Table, Column
from sqlalchemy.dialects.postgresql import UUID, TIMESTAMP, JSONB, INTEGER, VARCHAR, NUMERIC
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session


log = logging.getLogger(__name__)

base = declarative_base()


class TempJson(connectionDb):

    tempJsonStatus = Table(
        "temp_json_status", base.metadata
        , Column('id', INTEGER)
        , Column('uuid', UUID)
        , Column('date_current', TIMESTAMP)
        , Column('json_text', JSONB)
        , Column('api_name', VARCHAR)
        , Column('status', INTEGER)
    )

    def InsertResultJsonToDb(self, response, apiName):
        engine = super().createEngine()
        jsonString = json.dumps(response[0])
        currentDate = str(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        # self.dbconnect(self)
        with Session(engine) as session:
            statement = TempJson.tempJsonStatus.insert().values(
                date_current=currentDate,
                json_text=jsonString,
                api_name=apiName,
                status=response[1]
            )
            session.execute(statement)
            session.commit()
            session.close()


class Esp(connectionDb):

    espSensor = Table(
        "esp_sensor", base.metadata
        , Column('id', INTEGER)
        , Column('uuid', UUID)
        , Column('date_current', TIMESTAMP)
        , Column('pm_10', NUMERIC)
        , Column('pm_2_5', NUMERIC)
    )

    def espGetLastFromDataBase(self):
        engine = super().createEngine()
        with Session(engine) as session:
            data = session.query(self.espSensor.c.pm_10, self.espSensor.c.pm_2_5).order_by(self.espSensor.c.date_current.desc()).first()
        session.commit()
        session.close()
        return data

class Airly(connectionDb):

    airlySensor = Table(
        "airly_sensor", base.metadata
        , Column('id', INTEGER)
        , Column('uuid', UUID)
        , Column('date_current', TIMESTAMP)
        , Column('pm_10', NUMERIC)
        , Column('pm_2_5', NUMERIC)
    )

    def espGetLastFromDataBase(self):
        engine = self.createEngine()

        with Session(engine) as session:
            data = session.query\
                (self.airlySensor.c.pm_10, self.airlySensor.c.pm_2_5).order_by\
                (self.airlySensor.c.date_current.desc()).first()
        session.commit()
        session.close()
        return data
