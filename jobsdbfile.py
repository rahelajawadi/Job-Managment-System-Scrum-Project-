import sqlite3

# define a function to create a database
def createDB():
    # creating the connection
    db = sqlite3.connect("jobs.db")
    #create table
    #db.execute("create table userReg(ID INTEGER PRIMARY KEY AUTOINCREMENT,"
    #"name, password )")


    # insert values
    db.execute( "INSERT INTO userReg (name, password) "
    "VALUES('Rahela', '12345');")

    db.commit()

    cursor = db.execute("select * from userReg")
    for i in cursor:
        print(i)

    db.close()



createDB()