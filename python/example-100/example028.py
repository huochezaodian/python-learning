#!/usr/bin/python
# -*- coding: UTF-8 -*-

def age(n):
    if n == 1:
        return 10
    else:
        c = age(n-1) + 2
    return c

print '第五个人的年龄是：{}'.format(age(5))