#!/usr/bin/python
# -*- coding: UTF-8 -*-

y = int(raw_input('year:\n'))
m = int(raw_input('mouth:\n'))
d = int(raw_input('day:\n'))

months = (0,31,59,90,120,151,181,212,243,273,304,334)

if 0 < m <= 12:
    sum = months[m-1]
else:
    print 'please enter the correct month!'

sum += d
leap = 0

if (y%400 == 0) or ((y%4 == 0) and (y%100 != 0)):
    leap = 1

if (leap == 1) and (m > 2):
    sum += 1

print('it is the %dth day' % sum)