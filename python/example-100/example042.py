#!/usr/bin/python
# -*- coding: UTF-8 -*-
num1 = 2
num2 = 3
def autofunc():
    global num1
    num1 = 1
    num2 = 4
    print 'internal block num1 = %d, num2 = %d' % (num1, num2)
for i in range(3):
    print 'The num1 = %d, num2 = %d' % (num1, num2)
    autofunc()