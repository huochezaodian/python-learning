#!/usr/bin/python
# -*- coding: UTF-8 -*-

def getHight(start, distance):
    dic = {
        'distance':distance + start + start/2,
        'height':start/2
    }
    return dic

arr = {
    'distance':0,
    'height':float(100)
}

for i in range(10):
    arr = getHight(arr['height'], arr['distance'])

print '总高度是:{}\n第10次反弹高度是:{}'.format(arr['distance']-arr['height'],arr['height'])
