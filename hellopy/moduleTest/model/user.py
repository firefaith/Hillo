#!/usr/bin/python

class User:
  def __init__(self):
    self.name = ''
    self.email = ''
    self.pwd = ''
    pass

  def register(self,reg_info):
    self.name = reg_info['name']
    self.pwd = reg_info['pwd']

    print "register name:%s pwd:%s" % (self.name,self.pwd)

  def login(self,name,pwd):
    self.name = name
    self.pwd = pwd
    print name,"login"

  def logout(self):
    print "%s logout" % self.name

  def publishArticle(self):
    print "publish article"

  def updateArticle(self):
    print "update article"

  def deleteArticle(self):
    print "delete article"
