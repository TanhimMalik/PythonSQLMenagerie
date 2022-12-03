import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Malik__1982!",
    db="menagerie"
)

c = conn.cursor()

databases = ("show databases")
c.execute(databases)
for (databases) in c:
    print(databases[0])
