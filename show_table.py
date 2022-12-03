import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Malik__1982!",
    db="menagerie"
)

c = conn.cursor()


c.execute("DESCRIBE pet")
print(c.fetchall())
