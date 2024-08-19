from pymongo import MongoClient
import os
from dotenv import load_dotenv
load_dotenv()
def get_database()-> MongoClient:
   CONNECTION_STRING =   os.getenv("MONGO")
   client = MongoClient(CONNECTION_STRING)
   print("Connected to Database")
   return client['aitube']
  

db = get_database()