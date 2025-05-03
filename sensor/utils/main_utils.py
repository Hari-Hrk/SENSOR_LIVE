import yaml
import pandas as pd
import numpy as np
import os
import dill
import sys
from sensor.exception import SensorException
from sensor.logger import logging

def read_yaml_file(file_path:str)->dict:
    try:
        with open(file_path,'rb') as yaml_file:
            return yaml.safe_load(yaml_file)
    except Exception as e:
        raise SensorException(e,sys)