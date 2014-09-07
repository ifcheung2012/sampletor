# -*- coding: utf-8 -*-

__author__ = 'ifcheung'

import MySQLdb as db

conn = db.connect(host="localhost",user="root",passwd="123",db="ifcheung",charset="utf8")
cursor = conn.cursor()
sql = "select * from role"
result = cursor.execute(sql)

for row in cursor.fetchall():
    print row



import pymssql

connms = pymssql.connect(host='10.211.55.3',user='vb',password='vb',database='vbmis',timeout=10.0,login_timeout=5.0)
cursorms = connms.cursor()
cursorms.execute('select * from auths')

data = cursorms.fetchall()
print data



cursor.close()
conn.close()

cursorms.close()
connms.close()