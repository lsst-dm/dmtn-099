#!/usr/bin/env python

import uuid
import cx_Oracle

sql = "insert into seq(uuid) values (:uuid4)"

connection = cx_Oracle.connect("/@lsst_id_test")
connection.module = "SEQ"
connection.action = "SEQ_30x10000"
cur = connection.cursor()

dummy_uid = 'd79ec82f952243529d9a2d09be9f7ed9'

for i in range(0,10000):
    cur.execute(sql,uuid4=dummy_uid)

cur.close()
connection.commit()
