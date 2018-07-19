#!/usr/bin/python
from controller import db
class MongoDBApi(db.DBApi):
  def __init__(self):
    pass

  def insert(self,params=None):
    print "mongodb insert"
