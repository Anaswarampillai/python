import mysql.connector

mdb=mysql.connector.connect(
    host="localhost",
    user='root',
    password="7272"
)
print(mdb)