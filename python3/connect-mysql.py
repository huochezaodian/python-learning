#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import mysql.connector

config = {
	'user':'root',
	'password':'123456',
	'database':'test'
}

conn = mysql.connector.connect(**config)

cursor = conn.cursor()
sql = "insert into user (id, name) values ('2', 'john')"
cursor.execute(sql)
conn.commit()
cursor.close()

cursor = conn.cursor()
select_sql = "select * from user"
cursor.execute(select_sql)
values = cursor.fetchall()
print(values)
cursor.close()

conn.close()