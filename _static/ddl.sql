create table uuid1 
   (pk_col raw(16) not null enable, 
    uuid varchar2(128 byte), 
    constraint uuid1_pk primary key (pk_col) using index);
    
create table uuid4 
   (pk_col raw(16) not null enable, 
    uuid varchar2(128 byte), 
    constraint uuid4_pk primary key (pk_col) using index);
    
create or replace package pkg_butler_id as 
  c_butler_site_id constant number := 9999;
end pkg_butler_id;
/

create table seq
   (pk_col1 number not null enable, 
    pk_col2 number not null enable, 
    uuid varchar2(128 byte), 
    constraint seq_pk primary key (pk_col1,pk_col2) using index);

create sequence  seq_seq1 
  increment by 1 
  start with 1 cache 1000 
  noorder  nocycle  nokeep  noscale  global ;

create or replace package pkg_butler_id as 
  c_butler_site_id constant number := 9999;
end pkg_butler_id;

create or replace trigger seq_trg 
before insert on seq 
for each row 
begin
  <<column_sequences>>
  begin
    if inserting and :new.pk_col1 is null then
      select pkg_butler_id.c_butler_site_id, seq_seq1.nextval 
        into :new.pk_col1, :new.pk_col2 
        from sys.dual;
    end if;
  end column_sequences;
end;
/

alter trigger seq_trg enable;

