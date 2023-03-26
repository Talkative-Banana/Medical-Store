import mysql.connector as connector

class DB:
    def __init__(self):
        try:
            self.con = connector.connect(
                host='localhost',
                port='3306',
                user='root',
                password='1903',
                database='medical_store'
            )
            self.cur = self.con.cursor(buffered = True)

        except:
            print("Could not connect to database")