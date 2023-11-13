import pandas as pd 
import json
from datetime import datetime
import ssl
import numpy as np
import urllib3
from urllib3.util.ssl_ import create_urllib3_context

url1="https://api.stlouisfed.org/fred/series/observations?series_id=FEDFUNDS&api_key=10fc9856c73957751d46e9eea3eb32b8&file_type=json"

data = pd.read_json(url1)
# Récupération des observations
df=data['observations']
df= pd.json_normalize(df)
 # Conversion des données
df['realtime_start']=pd.to_datetime(df['realtime_start'], format="%Y-%m-%d")
df['realtime_end']=pd.to_datetime(df['realtime_end'], format="%Y-%m-%d")
df['date']=pd.to_datetime(df['date'], format="%Y-%m-%d")
df.value=df.value.astype(float).fillna(0.0)
filename='Data_Ocde'
path='D:/Données API/test/'+ filename + '.csv'
df.to_csv(path,index=False)