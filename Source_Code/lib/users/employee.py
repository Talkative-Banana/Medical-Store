class Employee:
    def __init__(self, ID, reg):
        self.ID = ID
        self.reg = reg
    
    def Verify(self, login_ID, login_pswd):
        return self.reg.Verify(login_ID, login_pswd, 1)
    
    def My_Acc(self):
        return self.reg.My_Acc(self.ID, 1)
    
    def Shop(self):
        return self.reg.Shop(1)
    
    def HandleOLAP(self):
        while True:
            print("1) Query outputting different consumers grouped as Sex and Age (Rollup)")
            print("2) Select Requirements with Type and Defcon (Rollup)")
            print("3) Query outputting different doctors grouped as Sex, Specialization and Qualifications (Rollup)")
            print("4) Union of different groups Including Sex, Specialization and qualifications (Grouping sets)")
            print("5) Cube Operation on Type and Defcon in niche requirements (Cube)")
            print("6) Cube Operation on Sex and Age in consumers (Cube)")
            print("7) Back\n")
            print("Note All columns appear in the defined order and last column is of Count")
            a = int(input())
            if(a > 0 and a < 7):
                self.reg.OLAP(a)
            elif(a == 7):
                break
            else:
                print("Invalid Input\n")

    def Triggers(self):
        while True:
            print("1) The Trigger Insures on every new addition of an entry to the database every consumer who has a prescription has atleast 10000 as sum insured (Minimum Plan)")
            print("2) Making sure that every insurance health insurance is atleat a year long")
            print("3) Making sure that every employee has password of length >= 8")
            print("4) Making sure that every consumer has password of length >= 8")
            print("5) Print all Triggers") 
            print("6) Back")
            a = int(input())
            if(a > 0 and a < 6):
                self.reg.Triggers(a)
            elif(a == 6):
                break
            else:
                print("Invalid Input\n")

    def SignUP(self, eid, name, pannumber, aadhaarnumber, age, dob, dpm, email, gender, phone, address):
        query = '''insert into employee (eid, ename, pannumber, aadhaarnumber, age, dob, department, email, gender, phone, address) values ({},'{}','{}','{}',{},'{}',{},'{}','{}','{}','{}')'''.format(eid, name, pannumber, aadhaarnumber, age, dob, dpm, email, gender, phone, address)
        try:
            self.reg.connection.cur.execute(query)
            self.reg.connection.con.commit()
        except:
            print("Error\n")
            
        while True:
            pswd = input("Enter pswd: ")
            try:
                query = '''insert into employee_credentials (employee_login_id, employee_login_password) values ({}, '{}')'''.format(eid, pswd)
                self.reg.connection.cur.execute(query)
                self.reg.connection.con.commit()
                print("Successfully Created Account\n")
                return
            except:
                print("Invalid password Length\n")

