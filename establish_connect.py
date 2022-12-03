import mysql.connector

# Creating connection object
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Malik__1982!",
    db="menagerie"
)

# Connection Success Check
print(mydb)
