def say():
  print "hello World"

def hello(x):
  try:
    def hi():
     print "hi", x
    hi()
  except Exception,e:
    print e
hello("hello")
