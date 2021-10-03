from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
import configparser

import pandas as pd
# obsluga zarządzania tabelami
Base = declarative_base()



def get_config_db():
    """

    :return:
    """
    config = configparser.ConfigParser()
    config.read('./config.ini')
    user = config.get("db", "user")
    passwd = config.get("db","passwd")
    host = config.get("db", "host")
    port = config.get("db", "port", raw=True)
    db_name = config.get("db", "db_name")

    return user,passwd,host,port,db_name

def dbconnect(func,config_list = get_config_db() ):
    """

    :param func:
    :param config_list:
    :return:
    """
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
def get_api_config(engine):
    df = pd.read_sql_query("select * from esp_sensor limit 1 ", engine)
    print(df.values.tolist())
    return df

