#!/usr/bin/env python

import uuid
import cx_Oracle

sql = "insert into uuid4(pk_col, uuid) values (:uuid4, :uuid4)"

connection = cx_Oracle.connect("/@lsst_id_test")
connection.module = "UUID4"
connection.action = "UUID4_30x10000"
cur = connection.cursor()

for i in range(0,10000):
    cur.execute(sql,uuid4=str(uuid.uuid4()).replace('-',''))

cur.close()
connection.commit()
