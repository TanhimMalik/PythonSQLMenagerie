import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Malik__1982!",
    db="menagerie"
)

c = conn.cursor()

c.execute("SELECT * FROM pet;")
table = c.fetchall()

for col in table:
    print(col[0], col[4])
