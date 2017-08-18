#!/usr/bin/python
# -*- coding: UTF-8 -*-

sum = 0
stage = 1

for i in range(1, 21):
    stage *= i
    sum += stage

print '1! + 2! + 3! + ... + 20! = %d' % sum