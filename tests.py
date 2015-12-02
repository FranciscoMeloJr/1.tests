from pymongo import MongoClient
from random import randint
import datetime
import urllib2
import time

#Connection to Mongo DB:
try:
    client = MongoClient()
    print "Connected successfully!!!"
except pymongo.errors.ConnectionFailure, e:
   print "Could not connect to MongoDB: %s" % e

db = client.mydb
collection = db.my_collection

#insertion:
start = time.time()

for x in range(0, 10):
    i = randint(0,1000)
    j = randint(0,1000)
   ##response = urllib2.urlopen('http://python.org/')
   #html = response.read()
    #doc = {"name":"Alberto","surname":"N","twitter":"@Altons","id":i*j,"date": datetime.datetime.utcnow()}
    doc = ["author": "Mike", "text": "Another post!", "tags": ["bulk", "insert"], "date": datetime.datetime(2009, 11, 12, 11, 14)},{"author": "Eliot","title": "MongoDB is fun","text": "and pretty easy too!","date": datetime.datetime(2009, 11, 10, 10, 45)}]
    #"page": html}
    collection.insert(doc)

end = time.time()
print end - start
#see the status:
client.database_names()
db.collection_names()
