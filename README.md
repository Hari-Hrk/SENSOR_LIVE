# SENSOR_LIVE
i want to create sensor fault prediction project

# steps
1. create env => conda create -p venv python==3.8 -y

2. run env ==> conda activate C:\Users\hi\Desktop\1\SENSORLIVE\venv

3. git clone

4. python setup.py install


## steps for send csv data to mongodb
- .env file
- load env files data in sensor/__init__.py
- sensor/config.py  -> load mongodb url
- utils_file

### steps for  mongodb to csv and data ingestion

- constant/env_variable.py & database.py
- configuration/mongodb_db_connection.py
- data_access / sensor_data.py
- sensor/constants/training_pipeline/__init__.py
- sensor/entity/artifact_entity.py
- sensor/enity/config_entity.py
- sensor/components/data_ingestion.py  -> this file mongodb data starts
- sensor/pipeline/training_pipeline.py
- main.py


# data validation part flow

- config/schema.yaml
- utils/main_utils.py
- constant/artifact & config entity
- sensor/component/data_validation
- pipeline/training_pipeline file update in run_pipeline function
- main.py

# data transmations
- constant/training_pipeline/__init__.py
- config/entity/artifact & config
- sensor/components/data_transformation
- utils/main_utils
- ml folder -> works on model folder like estimator.py
- component/data_transformation
- pipeline/training_pipeline


# model trainer
- constant/training_pipeline/__init__.py
- utls/main_utls.py --> load file function
- ml/metric
- config/entity/artifact & config
- components/model_trainer
- pipeline/training_pipeline

# model tevaluation
- constant/training_pipeline/__init__.py
- config/entity/artifact & config
- components/model_evaluation
