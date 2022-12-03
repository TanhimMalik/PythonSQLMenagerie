import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Malik__1982!",
    db="menagerie"
)

c = conn.cursor()


c.execute("SELECT * FROM pet WHERE species = 'dog' AND sex = 'f';")
table = c.fetchall()

for all in table:
    print(all[0], all[1], all[2], all[3], all[4], all[5])
