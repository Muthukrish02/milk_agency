import sqlite3

class DatabaseM:
    def __init__(self,db):

        self.con=sqlite3.connect(db)
        self.cur=self.con.cursor()
        sqlc="""CREATE TABLE IF NOT EXISTS Milkshop(
        id Integer Primary Key,
        userid text,
        phonenum binary,
        password text)"""

        self.cur.execute(sqlc)
        self.con.commit()
        '''sqlc = """CREATE TABLE IF NOT EXISTS Milk_Register(
                id Integer Primary Key,
                username text,
                phonenumber text,
                password text)"""'''
        #self.cur.execute(sqlc)
        #self.con.commit()
    def insert(self,userid,password,phonenum):

        self.cur.execute("Insert into Milkshop values(NULL,?,?,?)",(userid,password,phonenum))
        self.con.commit()
    def check_u(self,userid):
        self.cur.execute("SELECT userid FROM Milkshop")
        fdata=self.cur.fetchall()
        r=set(userid).issubset(fdata)

        self.con.commit()
        return r
    def check_p(self,userid):
        self.cur.execute("SELECT password FROM Milkshop")
        fdata=self.cur.fetchall()
        r=set(userid).issubset(fdata)

        self.con.commit()
        return r
    def insR(self,usn,ph,pwd):
        self.cur.execute("Insert into Milk_register values(null,?,?,?)",(usn,ph,pwd))
        self.con.commit()



