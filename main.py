import sqlite3

correct_pass = '1234'

password = input('What is your password\n')

def login():
    if password == correct_pass:
        print("""
              S = save img
              O = open file
              """)
        userinput = input(':')
    else:
        print('try again')
    if userinput == 'S':
        input('what is the file name :')
login()

# connecting the db server
conn = sqlite3.connect('secretfiles.db') 


curs = conn.cursor()

# making the database
curs.execute("""CREATE TABLE user (
        Password text,
        Files BLOB
        )""")

# adding dummy info
curs.execute("INSERT INTO user VALUES ('1234', 'file.png')")

curs.execute("SELECT * FROM user")

print(curs.fetchone())

conn.commit()

#closing the db connection
conn.close()



