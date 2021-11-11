import configparser
import os

from dotenv import load_dotenv

from sqlalchemy import create_engine

class connectionDb():

    def createEngine(self):
        """
        getting host from config.ini file
        and data required to connect to the database from environment variables .env
        :return:  SqlAlchemy engine
        """
        # Config.ini
        config = configparser.ConfigParser()
        config.read('./config.ini')
        # ENV
        load_dotenv()
        dbHost = config.get("db", "host")
        dbUser = os.getenv("DB_USER")
        dbPasswd = os.getenv("DB_PASSWD")
        dbPort = os.getenv("DB_PORT")
        dbName = os.getenv("DB_NAME")
        engine = create_engine(
            'postgresql://' + dbUser + ':' + dbPasswd + \
            '@' + dbHost + ':' + dbPort + '/' + dbName
        )
        return engine