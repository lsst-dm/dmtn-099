#!/usr/bin/env python

import sqlite3

site_id          = 9999
batch_id_size    = 100
table_name       = 't'
sqlite_filename  = 'test.sqlite3'

sql_upd_max_id   = """update id_tracker 
                        set curr_max_id = curr_max_id + ?
                        where table_name = ?"""

sql_get_max_id   = """select curr_max_id 
                        from id_tracker 
                        where table_name = ?"""

sql_ins_t        = "insert into t(id, site_id) values(?,?)"

trying_to_insert = True

while trying_to_insert:
    try:  
        with sqlite3.connect(sqlite_filename) as conn:
            cur = conn.cursor()
            cur.execute ("begin exclusive transaction")
            cur.execute(sql_upd_max_id, [batch_id_size, table_name])
            cur.execute(sql_get_max_id, table_name)
            max_id = cur.fetchone()[0] + 1
            t_id_batch = [(new_id, site_id) for new_id in range(max_id - batch_id_size , max_id)]
            cur.executemany(sql_ins_t, t_id_batch)
            trying_to_insert = False

    except sqlite3.OperationalError:
        print("Database was locked")



  

