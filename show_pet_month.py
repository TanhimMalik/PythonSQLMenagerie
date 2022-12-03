import mysql.connector
from tabulate import tabulate

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Malik__1982!",
    db="menagerie"
)

c = conn.cursor()

c.execute("SELECT name, birth, MONTH(birth) FROM pet;")
table = c.fetchall()

print(tabulate(table, headers=[
      'name', 'birth', 'MONTH(birth)'], tablefmt='psql'))
