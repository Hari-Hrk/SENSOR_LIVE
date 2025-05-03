import sys
from typing import Optional
import numpy as np
import pandas as pd
import json
from sensor.exception import SensorException
from sensor.constant.database import DATABASE_NAME
from sensor.configuration.mongodb_db_connection import MongoDBClient

class SensorData:
    def __init__(self):
        try:
            self.mongo_client = MongoDBClient(database_name=DATABASE_NAME)
        except Exception as e:
            raise SensorException(e,sys)
        
    def save_csv_file(self,file_path,collection_name:str,database_name:Optional[str]=None):
        try:
            df = pd.read_csv(file_path)
            df.reset_index(drop=True,inplace=True)
            records = list(json.loads(df.T.to_json()).values())
            if database_name is None:
                collection = self.mongo_client.database[collection_name]
            else:
                collection = self.mongo_client[database_name][collection_name]
            collection.insert_many(records)
            return len(records)
        except Exception as e:
            raise SensorException(e,sys)