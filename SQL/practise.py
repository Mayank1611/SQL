import sqlite3
connection=sqlite3.connect('demo.db')
crsr=connection.cursor()

sql_create="""CREATE TABLE student(
            studid integer(50) PRIMARY KEY,
            name VARCHAR(200),
            dob DATE(200),
            reg time DATETIME
            );"""
crsr.execute(sql_create)

sql_insert="""INSERT INTO student VALUES(:1,:2,:3,:4);"""
data=[
    (18056,'Sanju','2002-10-26','2022-10-10 10:00:00'),
    (10456,'lanju','2008-10-26','2022-10-15 10:00:00'),
    (1056,'tanju','2010-10-26','2022-10-18 10:00:00'),
]
crsr.executemany(sql_insert,data)




# sql_select=("SELECT *FROM student WHERE studid='1056'")
# crsr.execute(sql_select)
# sql_select=("SELECT *FROM student ORDER BY dob")
# crsr.execute(sql_select)
# sql_update=("UPDATE student SET name='ranju' WHERE studid=1056")
# crsr.execute(sql_update)
# sql_delete=("DELETE FROM student WHERE studid=1056")
# crsr.execute(sql_delete)

# sql_add=("ALTER TABLE student ADD country VARCHAR(200)")
# crsr.execute(sql_add)
# sql_update=("UPDATE student SET country='INDIA' WHERE studid=1056")
# crsr.execute(sql_update)
sql_delete=("ALTER TABLE student DROP COLUMN dob")
crsr.execute(sql_delete)

sql_select=("SELECT *FROM student ")
crsr.execute(sql_select)

ans=crsr.fetchall()
for i in ans:
    print(i)


connection.commit()
connection.close()
