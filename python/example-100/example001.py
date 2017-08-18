#!/usr/bin/python
# -*- coding: UTF-8 -*-

count = 1

for i in range(1, 5):
    for j in range(1, 5):
        for k in range(1, 5):
            if i != j != k:
                count += 1
                print i, j, k

print("能组成%d个互不相同且无重复数字的三位数" % count)