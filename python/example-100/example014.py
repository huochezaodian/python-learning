#!/usr/bin/python
# -*- coding: UTF-8 -*-

num = int(raw_input('please enter a number:'))

def reduceNum(n):
    if not isinstance(n, int) or n <= 0 :
        print 'please enter an integer greater than 0 !'
        exit(0)
    print '{} ='.format(n),
    if n in [1, 2, 3] :
        print '{}'.format(n)
    while n not in [1] :
        for i in range(2, n+1) :
            if n%i == 0 :
                n /= i
                if n == 1 :
                    print '{}'.format(i)
                else :
                    print '{} *'.format(i),
                break

reduceNum(num)
