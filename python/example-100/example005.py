#!/usr/bin/python
# -*- coding: UTF-8 -*-

arr = []

def reorder(a,b):
    print a, b
    return b - a

for i in range(1, 4):
    x = int(raw_input('please enter a number:'))
    arr.append(x)

arr.sort(reorder)

print arr
