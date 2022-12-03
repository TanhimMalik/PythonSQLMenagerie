import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Malik__1982!",
    db="menagerie"
)

c = conn.cursor()


def create_table():

    c.execute('DROP TABLE IF EXISTS pet')
    c.execute('CREATE TABLE pet \
            ( \
                name  VARCHAR(20), \
                owner VARCHAR(20), \
                species VARCHAR(20), \
                sex CHAR(10), \
                birth DATE, \
                death DATE \
            )'
              )
