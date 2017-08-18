#!/usr/bin/python
# -*- coding: UTF-8 -*-

def getFactor(n):
    arr = []
    for i in range(1, n) :
        if n%i == 0 :
            arr.append(i)
    return arr

def handleNum(n):
    for i in range(2, n+1):
        factors = getFactor(i)
        sum = reduce(lambda x,y:x+y , factors)
        if sum == i :
            print i
            print factors

handleNum(1000)