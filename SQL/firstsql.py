import sqlite3
connection=sqlite3.connect("sanju.db")
crsr=connection.cursor()

sql_create="""CREATE TABLE job(
              job_id integer(11) PRIMARY KEY,
              name varchar(50),
              salery integer(15)
            );"""
crsr.execute(sql_create)

sql_insert="""INSERT INTO job VALUES(:1,:2,:3);"""
data=[(1012,"Sanju",180000),
    (1021,"Puva",12000),
    (1245,"dj",1000)]
crsr.executemany(sql_insert, data)

# sql_update="""UPDATE job SET salery=(salery+1000)"""
# crsr.execute(sql_update)
# sql_delete="""DELETE FROM job WHERE job_id=1021"""
# crsr.execute(sql_delete)

# sql_add="""ALTER TABLE job ADD country varchar(200)"""
# crsr.execute(sql_add)
# sql_update="""UPDATE job SET country='India' WHERE job_id=1012"""
# crsr.execute(sql_update)

# sql_delete="""ALTER TABLE job DROP COLUMN salery"""
# crsr.execute(sql_delete)
sql_select=("SELECT *FROM job")
crsr.execute(sql_select)

ans=crsr.fetchall()
for i in ans:
    print(i)

connection.commit()
connection.close()

