#!/usr/bin/python
# -*- coding: UTF-8 -*-

a,b = 2.0,1.0
l = []

for i in range(20):
    l.append(a/b)
    a,b = a+b,a

print reduce(lambda x,y:x+y , l)
print l