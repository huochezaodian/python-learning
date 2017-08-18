#!/usr/bin/python
# -*- coding: UTF-8 -*-

i = int(raw_input('净利润:'))

arr = [1000000,600000,400000,200000,100000,0]
rat = [0.01,0.015,0.03,0.05,0.075,0.1]
bonus = 0

for idx in range(0, len(arr)):
    if (i > arr[idx]) :
        bonus += (i - arr[idx]) * rat[idx]
        print bonus
        i = arr[idx]

print('应该发的奖金数是%d元' % bonus)