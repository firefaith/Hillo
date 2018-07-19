#!/usr/bin/python
from model import user

u1 = user.User()
reg_info = {'name':'Mike','pwd':'123456'}
u1.register(reg_info)
u1.login("Mike",'123456')
u1.publishArticle()
u1.updateArticle()
u1.deleteArticle()


from controller import mongoDB

m1 = mongoDB.MongoDBApi()
m1.insert()
m1.update()
