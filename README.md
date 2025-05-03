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

- config/schema.yaml
- constant/env_variable.py & database.py
- configuration/mongodb_db_connection.py
- data_access / sensor_data.py
- config/schema.yaml  == out of sensor folder
- sensor/constants/training_pipeline/__init__.py
- sensor/entity/artifact_entity.py
- sensor/enity/config_entity.py
- sensor/components/data_ingestion.py  -> this file mongodb data starts
- sensor/pipeline/training_pipeline.py
- main.py