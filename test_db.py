from pymongo import MongoClient
import certifi

uri = "mongodb+srv://samruddhimuley139_db_user:ckUV7Sn89ALBvd9B@cluster0.ltglgak.mongodb.net/?appName=Cluster0"

client = MongoClient(uri, tlsCAFile=certifi.where())
print("Connected! Databases:", client.list_database_names())
