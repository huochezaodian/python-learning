#!/usr/bin/python
# -*- coding: UTF-8 -*-

for i in range(2, 85, 2):
    if 168 % i == 0:
        j = 168 / i;
        if i > j and (j % 2 == 0):
            m = (i + j) / 2
            n = (i - j) / 2
            x = n * n - 100
            print(x)
