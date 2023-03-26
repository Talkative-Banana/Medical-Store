class Consumer:
    def __init__(self, ID, reg):
        self.ID = ID
        self.reg = reg

    def Verify(self, login_id, login_pwd):
        return self.reg.Verify(login_id, login_pwd, 0)
    
    def My_Acc(self):
        return self.reg.My_Acc(self.ID, 0)
    
    def Shop(self):
        return self.reg.Shop(0)
    
    def SignUP(self, cid, pannumber, name, gender, age, email, phone):
        query = '''insert into consumer (cid, pannumber, cname, sex, age, emailid, phone) values ({}, '{}', '{}', '{}', {}, '{}', '{}')'''.format(cid, pannumber, name, gender, age, email, phone)
        try:
            self.reg.connection.cur.execute(query)
            self.reg.connection.con.commit()
        except:
            print("Error\n")
            
        while True:
            pswd = input("Enter pswd: ")
            try:
                query = '''insert into consumer_credentials (consumer_login_id, consumer_login_password) values ({}, '{}')'''.format(cid, pswd)
                self.reg.connection.cur.execute(query)
                self.reg.connection.con.commit()
                print("Successfully Created Account\n")
                return
            except:
                print("Invalid password Length\n")