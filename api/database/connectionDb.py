import configparser
import os

from dotenv import load_dotenv
from sqlalchemy import create_engine

class connectionDb():

    def __init__(self):
        self.engine
        self.dbHost
        self.dbUser
        self.dbPasswd
        self.dbPort
        self.dbName

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
        self.dbHost = config.get("db", "host")
        self.dbUser = os.getenv("DB_USER")
        self.dbPasswd = os.getenv("DB_PASSWD")
        self.dbPort = os.getenv("DB_PORT")
        self.dbName = os.getenv("DB_NAME")
        engine = create_engine(
            'postgresql://' + self.dbUser + ':' + self.dbPasswd + \
            '@' + self.dbHost + ':' + self.dbPort + '/' + self.dbName
        )
        return engine