#!/usr/bin/python
# -*- coding: UTF-8 -*-

str = raw_input('please enter a line of characters:')

letters = space = digit = others = 0

for c in str :
    if c.isalpha() :
        letters += 1
    elif c.isdigit() :
        digit += 1
    elif c.isspace() :
        space += 1
    else:
        others += 1

print 'char = %d,space = %d,digit = %d,others = %d' % (letters, space, digit, others)