#!/usr/bin/python
# -*- coding: UTF-8 -*-

for i in range(1,8):
    if i in [1, 7]:
        print '{:^7s}'.format('*')
    elif i in[2, 6]:
        print '{:^7s}'.format('***')
    elif i in [3, 5]:
        print '{:^7s}'.format('*****')
    else:
        print '{:^7s}'.format('*******')