import mysql.connector as sql
db=sql.connect(host="localhost",user="root",passwd="xiibk",database="phonebook")
cursor=db.cursor()
cursor.execute("CREATE TABLE contact(sno int auto_increment Primary Key,name varchar(100),number varchar(10))")
