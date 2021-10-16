import configparser
import json
from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy import Table,Column
from sqlalchemy.dialects.postgresql import UUID,TIMESTAMP,JSONB,INTEGER,VARCHAR
from sqlalchemy.ext.declarative import declarative_base



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

    def __init__(self):
        pass

    def config_db(self):
        config = configparser.ConfigParser()
        config.read('./config.ini')
        user = config.get("db", "user")
        passwd = config.get("db","passwd")
        host = config.get("db", "host")
        port = config.get("db", "port", raw=True)
        db_name = config.get("db", "db_name")
        return user,passwd,host,port,db_name

    def dbconnect(self):
        config_list = self.config_db(self)
        user = config_list[0]#self.user
        passwd = config_list[1]#self.passwd
        host = config_list[2]#self.host
        port = config_list[3]#self.port
        db = config_list[4]#self.db_name
        engine = create_engine(
            'postgresql://' + user + ':' + passwd + '@' + host + ':' + port + '/' + db
        )
        return  engine



    def airly_insert(self, json_airly):
        engine = self.dbconnect(self)
        json_string = json.dumps(json_airly)
        current_date_string = str(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        api_name = 'airly'
        #self.dbconnect(self)
        statment = self.j_table.insert().values(
            date_current=current_date_string,
            json_text=json_string,
            api_name=api_name,
            status='200'
        )
        engine.execute(statment)
        print('INSET AIRLY- TRUE ' + current_date_string)
        return json_airly


    # def dbconnect(self,func ):
    #     def wrapper(*args,**kwargs):
    #         config_list = self.config_db()
    #         user = config_list[0]
    #         passwd = config_list[1]
    #         host = config_list[2]
    #         port = config_list[3]
    #         db = config_list[4]
    #         engine = create_engine('postgresql://'+user+':'+passwd+'@'+host+':'+port+'/'+db)
    #         return func(engine)
    #     return wrapper

    # @dbconnect
    # def airly_insert(self,engine):
    #     #json_airly = airly.get_airly_results()
    #     json_string = json.dumps(json_airly)
    #     current_date_string = str(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    #     api_name = 'airly'
    #     statment = self.j_table.insert().values(
    #         date_current=current_date_string
    #         , json_text=json_string
    #         , api_name=api_name
    #         , status='200'
    #     )
    #     engine.execute(statment)
    #     print('INSET AIRLY- TRUE ' + current_date_string)
    #     return json_airly
    #
    # @dbconnect
    # def esp_insert(self,engine,json_esp):
    #     #json_esp = esp.get_esp_results()
    #     json_string = json.dumps(json_esp)
    #     current_date_string = str(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    #     api_name = 'esp'
    #     statment = self.j_table.insert().values(
    #          date_current = current_date_string
    #         ,json_text= json_string
    #         ,api_name =api_name
    #         ,status = '200'
    #     )
    #     engine.execute(statment)
    #     print('INSET ESP- TRUE ' + current_date_string)
    #     return json_esp