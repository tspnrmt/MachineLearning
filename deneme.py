import pymongo
from pymongo import MongoClient
client = MongoClient('mongodb://localhost:27017/')

# DB From M.C. Ganiz
db = client['Response']

#Read only JsonResponse field
print ("Data reading")
cursor = db.Response.find({}, {"JsonResponse" : 1, "_id":0})
print ("Finished reading")
#new DB 
dbNew = client['ResponseInsert'] 

print ("Data inserting")
for document in cursor:
    # print(document)
    # DB insert to Yeni collection
    dbNew.Yeni.insert(document)
print ("Data inserted")