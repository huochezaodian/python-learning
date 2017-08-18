#!/usr/bin/python
# -*- coding: UTF-8 -*-

num = raw_input('please enter a number:')
count = int(raw_input('please enter the number of times:'))

sum = []

for i in range(count):
    v = num * (i+1)
    print v
    sum.append(int(v))

s = reduce(lambda x,y:x+y , sum)

print '计算和是:\t%d' % s