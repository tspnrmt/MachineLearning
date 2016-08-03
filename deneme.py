print ("Hello World!")
import pymongo
from pymongo import MongoClient
client = MongoClient('mongodb://localhost:27017/')
db = client['Response']
cursor = db.Response.find({}, {"JsonResponse" : 1, "_id":0})
db2 = client['ResponseInsert'] 
for document in cursor:
    print(document)
    db2.Yeni.insert(document)
    break