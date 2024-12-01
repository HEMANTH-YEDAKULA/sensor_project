pip install pymongo

from pymongo.mongo_client import MongoClient
import pandas as pd
import json

#url
uri="mongodb+srv://imran:AyvISySxh9BC3QiU@cluster0.fv0lm61.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

#create a new client and connectt to server
client = MongoClient(uri)

#create database name and collection name
DATABASE_NAME="pwskills"
from pymongo.mongo_client import MongoClient
import pandas as pd
import json

#url
uri="mongodb+srv://HEMANTH:pyyApc9oTnUDxKhh@cluster0.sf7zt.mongodb.net/?retryWrites=true&w=majority"

#create a new client and connectt to server
client = MongoClient(uri)

# #create database name and collection name
DATABASE_NAME="pwskil"
COLLECTION_NAME='waferfault'

df=pd.read_csv("C:\Users\hh364\OneDrive\Desktop\sensorproject\notebooks\wafer_23012020_041211.csv")

df=df.drop("Unnamed: 0",axis=1)
df

json_record=list(json.loads(df.T.to_json()).values())

client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)
