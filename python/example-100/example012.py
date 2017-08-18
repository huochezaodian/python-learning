#!/usr/bin/python
# -*- coding: UTF-8 -*-

import math

l = []

for i in range(101, 201):
    for j in range(2, int(math.sqrt(i))+1):
        if i%j == 0 :
            break
    else :
        l.append(i)

print '101到200之间一共有%d个素数，分别为：' % len(l), l