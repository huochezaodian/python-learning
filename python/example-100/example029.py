#!/usr/bin/python
# -*- coding: UTF-8 -*-

num = raw_input('please enter a number:')

print '长度是%d' % len(num)

for i in range(len(num)-1,-1,-1):
    print num[i],