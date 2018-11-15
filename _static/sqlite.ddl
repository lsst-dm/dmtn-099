CREATE TABLE t(id integer not null,
    site_id integer not null,
    primary key (id, site_id));

CREATE TABLE id_tracker(table_name varchar(100),
    curr_max_id integer, primary key (table_name));

INSERT INTO id_tracker VALUES('t',1);


