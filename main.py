import sys
import os
from sensor.exception import SensorException
from sensor.logger import logging
from sensor.configuration.mongodb_db_connection import MongoDBClient

def test():
    try:
        logging.info("error is here due to division by zero error")
        a = 1/0
    except Exception as e:
        raise SensorException(e,sys)

if __name__ == "__main__":
    try:
        MongoDBClient()
    except Exception as e:
        print(e)
        #raise SensorException(e,sys)