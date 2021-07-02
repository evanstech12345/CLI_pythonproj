import sqlite3

correct_pass = '1234'

password = input('What is your password\n')



def create_database():
# connecting the db server
    conn = sqlite3.connect('secretfiles.db') 


    curs = conn.cursor()

# making the database
    curs.execute("""CREATE TABLE IF NOT EXISTS img (
        Files BLOB
        )""")

# adding dummy info
    curs.execute(f"INSERT INTO img VALUES ({path})")

    curs.execute("SELECT * FROM img")

    print(curs.fetchone())

    conn.commit()

#closing the db connection
    conn.close()


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
        global path 
        path = input('what is the file path : ')
login()
create_database()





