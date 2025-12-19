import os
from pymongo import MongoClient
import certifi

MONGO_URI = os.environ.get("MONGO_URI")

client = MongoClient(
    MONGO_URI,
    tlsCAFile=certifi.where()
)

db = client["flipr_db"]
