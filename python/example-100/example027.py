#!/usr/bin/python
# -*- coding: UTF-8 -*-

def reverse(str, l):
    if l == 0:
        return
    print str[l-1]
    reverse(str, l-1)

str = raw_input('please enter a string:')

reverse(str, len(str))