#!/usr/bin/python

def h():
  print "first line"
  m = yield 1
  print "second line"
  n = yield 2
  print "third line"
  o = yield 3
  print "end"

print "call h() ..."
h() #nothing will produce

print "call next ..."
c = h()
item = c.next()
for item in c:
  pass
print "for item",item
a = c.next()
print "return ",a
a = c.next()
a = c.next()
a = c.next()
