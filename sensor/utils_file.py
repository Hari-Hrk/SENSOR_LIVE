import numpy as np
import json
import sys
import pandas as pd
from sensor.exception import SensorException
from sensor.config import mongo_client

def dump_csv_file_to_mongodb_collecton(file_path:str,database_name:str,collection_name:str)->None:
    try:
        df = pd.read_csv(file_path)
        #print(f"file_path is ===> {file_path}, db name : {database_name} ,collection name : {collection_name}")
        df.reset_index(drop=True,inplace=True)
        #print('mongoclient is ==========> ',mongo_client)
        json_records = list(json.loads(df.T.to_json()).values())
        mongo_client[database_name][collection_name].insert_many(json_records)
    except Exception as e:
        raise SensorException(e,sys)