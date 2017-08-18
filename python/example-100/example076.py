#!/usr/bin/python
# -*- coding: UTF-8 -*-

def peven(n):
    s = 0
    for i in range(2, n+1, 2):
        s += 1.0/i
    else:
        return s

def podd(n):
    s = 0
    for i in range(1, n+1, 2):
        s += 1.0/i
    else:
        return s

if __name__ == '__main__':
    num = int(raw_input('please enter a number:'))
    if num%2 == 0:
        s = peven(num)
    else:
        s = podd(num)
    print '和是:%.10f' % s