#!/usr/bin/python
# -*- coding: UTF-8 -*-

def rabbit(m):
    if m == 1 :
        return [1]
    if m == 2 :
        return [1, 1]
    count = [1, 1]
    for i in range(2, m+1):
        count.append(count[-1] + count[-2])
    return count

def printCount(m):
    arr = rabbit(m)
    for i in range(0, m):
        print '第 %d 个月有 %d 对兔子' % (i+1, arr[i])

printCount(100)