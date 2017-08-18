#!/usr/bin/python
# -*- coding: UTF-8 -*-

def factorial(m):
    if m == 1:
        return 1
    return m * factorial(m-1)

print '5! = %d' % factorial(5)