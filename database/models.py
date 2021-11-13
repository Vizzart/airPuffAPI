# coding=utf-8
import logging
import json
from datetime import datetime

from database.connectionDb import connectionDb
from sqlalchemy import Table, Column, func
from sqlalchemy.dialects.postgresql import UUID,\
TIMESTAMP, JSONB, INTEGER, VARCHAR, NUMERIC, TEXT
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session

log = logging.getLogger(__name__)

base = declarative_base()

class TempSensorData(connectionDb):

    tempJsonStatus = Table(
        "temp_sensor_data", base.metadata
        , Column('id', INTEGER)
        , Column('uuid', UUID)
        , Column('date_current', TIMESTAMP)
        , Column('json_text', JSONB)
        , Column('api_name', VARCHAR)
        , Column('status', INTEGER)
    )

    def InsertResultJsonToDataBase(self, response, apiName):
        engine = super().createEngine()
        jsonString = json.dumps(response[0])
        currentDate = str(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        # self.dbconnect(self)
        with Session(engine) as session:
            statement = TempSensorData.tempJsonStatus.insert().values(
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
    espCurrentJsonLastView = Table(
        "esp_current_json_last_view", base.metadata
        , Column('sensorValue', JSONB)
    )
    def espGetLastView(self):
        engine = super().createEngine()
        try:
            with Session(engine) as session:
                data = session.query(self.espCurrentJsonLastView)
            session.commit()
            session.close()
            return data, 200
        except:
            return data, 500

class Airly(connectionDb):

    airlyForecastJsonLastView = Table(
        "airly_forecast_json_last_view", base.metadata
        , Column('forecast', JSONB)
    )
    airlyHistoryJsonLastView = Table(
        "airly_history_last_json_view", base.metadata
        , Column('history', JSONB)
    )
    airlyCurrentLastView = Table(
        "airly_current_json_last_view", base.metadata
        , Column('current', JSONB)
    )

    def airlyGetLastJsonView(self):
        engine = self.createEngine()
        try:
            with Session(engine) as session:
                data = session.query(self.airlyCurrentLastView)
            session.commit()
            session.close()
            return data, 200
        except:
            return data, 500

    def airlyGetForecastLastJsonView(self):
        engine = self.createEngine()
        try:
            with Session(engine) as session:
                rows = session.query(
                    func.array_agg(self.airlyForecastJsonLastView.c.forecast).label("forecast"))
            session.commit()
            session.close()
            data = []
            for row in rows:
                data.append(row)
            return data, 200
        except:
            return data, 500

    def airlyGetHistoryJsonLastView(self):
        engine = self.createEngine()
        try:
            with Session(engine) as session:
                rows = session.query(
                    func.array_agg(self.airlyHistoryJsonLastView.c.history).label("history"))
            session.commit()
            session.close()
            data = []
            for row in rows:
                data.append(row)
            return data, 200
        except:
            return data, 500

class Norms(connectionDb):
    norms = Table(
        "norms"
        , base.metadata
        , Column('id', INTEGER)
        , Column('uuid_', UUID)
        , Column('date_current', TIMESTAMP)
        , Column('pm_10_norm', NUMERIC)
        , Column('pm_2_5_norm', NUMERIC)
        , Column('description', TEXT)
        , schema = "config"
    )

    def getConfigNorms(self):
        engine = self.createEngine()
        try:
            with Session(engine) as session:
                rows = session.query(self.norms)

            session.commit()
            session.close()
            data = []
            for row in rows:
                data.append(row)
            return data, 200
        except:
            return data, 500