import sys
import os
from sensor.exception import SensorException
from sensor.logger import logging
from sensor.utils_file import dump_csv_file_to_mongodb_collecton
from sensor.pipeline.training_pipeline import TrainPipeline




if __name__ == "__main__":
    training_pipeline = TrainPipeline()
    training_pipeline.run_pipeline()
    













# if __name__ == "__main__":
#     try:
#         file_path = "aps_failure_training_set1.csv"
#         database_name = "ineuron"
#         collection_name='sensor'
#         dump_csv_file_to_mongodb_collecton(file_path,database_name,collection_name)
#     except Exception as e:
#         print(e)
        #raise SensorException(e,sys)

# def test():
#     try:
#         logging.info("error is here due to division by zero error")
#         a = 1/0
#     except Exception as e:
#         raise SensorException(e,sys)

