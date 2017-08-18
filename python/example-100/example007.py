#!/usr/bin/python
# -*- coding: UTF-8 -*-

import  copy

a = [1, 3, 3]

b = a[:]

c = copy.copy(a)

b[0] = 4

c[1] = 4

print a, b, c