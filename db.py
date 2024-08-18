from pymongo import MongoClient
import os
def get_database()-> MongoClient:
   CONNECTION_STRING =   os.getenv("MONGO")
   client = MongoClient(CONNECTION_STRING)
   print("Connected to Database")
   return client['aitube']
  

db = get_database()