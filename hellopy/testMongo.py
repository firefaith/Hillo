#!/usr/bin/python

import pymongo
from pymongo import MongoClient
client = MongoClient()
client = MongoClient('localhost', 27017)
db = client.test_database
# db = client['test-database']

collection = db.test_collection
#collection = db['test-collection']

import datetime
post = {"author": "Mike",
        "text": "My first blog post!",
        "tags": ["mongodb", "python", "pymongo"],
        "date": datetime.datetime.utcnow()}

posts = db.posts
# insert 
if 1==0:
  post_id = posts.insert_one(post).inserted_id
  print post_id
# show all collection
print db.collection_names(include_system_collections=False)

# query
import pprint
pprint.pprint(posts.find_one())
pprint.pprint(posts.find_one({"author": "Mike"}))

# insert bulk
new_posts = [{"author": "Mike",
              "text": "Another post!",
              "tags": ["bulk", "insert"],
              "date": datetime.datetime(2009, 11, 12, 11, 14)},
             {"author": "Eliot",
              "title": "MongoDB is fun",
              "text": "and pretty easy too!",
              "date": datetime.datetime(2009, 11, 10, 10, 45)}]
	 
if 1==0:
  result = posts.insert_many(new_posts)
  print result.inserted_ids

# find many documents
for post in posts.find({"author": "Mike"}):
  pprint.pprint(post)
