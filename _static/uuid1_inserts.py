#!/usr/bin/env python

import uuid
import cx_Oracle

sql = "insert into uuid1(pk_col, uuid) values (:uuid1, :uuid1)"

connection = cx_Oracle.connect("/@lsst_id_test")
connection.module = "UUID1"
connection.action = "UUID30x10000"
cur = connection.cursor()

for i in range(0,10000):
    cur.execute(sql,uuid1=str(uuid.uuid1()).replace('-',''))

cur.close()
connection.commit()
