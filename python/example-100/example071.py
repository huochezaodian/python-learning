#!/usr/bin/python
# -*- coding: UTF-8 -*-

N = 3
students = []

for i in range(N):
    students.append(['','',[]])

def input_stu(stus):
    for i in range(N):
        stus[i][0] = raw_input('num:')
        stus[i][1] = raw_input('name:')
        for j in range(N):
            stus[i][2].append(int(raw_input('score:')))

def output_stu(stus):
    for i in range(N):
        print '\nnum:%-6s\tname:%-6s' % (stus[i][0], stus[i][1])
        for j in range(N):
            print 'score:{:<6d}'.format(stus[i][2][j])

if __name__ == '__main__':
    input_stu(students)
    print students
    output_stu(students)
