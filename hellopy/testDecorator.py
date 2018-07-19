#!/usr/bin/python

def sayHello(help):
  def _run():
    print "Hello"
    help()
  return _run

def help1():
  print "1.lend me some money."

@sayHello
def help2():
  print "2.lend me some money."
 
help1()
help2()
