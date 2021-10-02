import json
import sqlalchemy
from flask import Flask
from sqlalchemy import Table,Column
from sqlalchemy.dialects.postgresql import UUID,TIMESTAMP,JSON,INTEGER

from db_con import con
from airly import airly


app = Flask(__name__)

con.get_api_config()
print(airly.get_airly_results())


if __name__ == '__main__':
    app.debug = False
    app.run(host="localhost", port=8989)
