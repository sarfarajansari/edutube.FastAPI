from pymongo import MongoClient

def get_database()-> MongoClient:
   CONNECTION_STRING =    "mongodb+srv://p:zMtpS9kUGUwKmppe@mydbcluster.8axgt8u.mongodb.net/"
   client = MongoClient(CONNECTION_STRING)

   return client['aitube']
  

db = get_database()