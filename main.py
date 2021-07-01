import click
import sqlite3

conn = sqlite3.connect('secretfiles.db') 

curs = conn.cursor()

curs.execute("""CREATE TABLE user (
        Password text,
        Files BLOB
        )""")


conn.commit()
conn.close()

print('code is working')