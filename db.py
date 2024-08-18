from pymongo import MongoClient
import os
def get_database()-> MongoClient:
   CONNECTION_STRING =   os.getenv("MONGO")
   client = MongoClient(CONNECTION_STRING)

   return client['aitube']
  

db = get_database()