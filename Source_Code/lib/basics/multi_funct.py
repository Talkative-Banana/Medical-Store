class Multi_Functional:
    def __init__(self, DBMS):
        self.connection = DBMS

    def pprint(self, lst):
        if len(lst) == 7:
            # Consumer
            print('''\ncid: {}\nPan Number: {}\nName: {}\nSex: {}\nAge: {}\nEmail: {}\nPhone: {}\n'''.format(lst[0], lst[1], lst[2], lst[3], lst[4],lst[5], lst[6]))
        elif(len(lst) == 8):
            # Drug
            try:
                print('''\ndid: {}\nName: {}\nSalts: {}\nManufacturing Date: {}\nProducer: {}\nPrice: {}\nQuantity: {}\nCategory: {}\n'''.format(lst[0], lst[1].split()[1], lst[2], lst[3], lst[4],lst[5], lst[6], lst[7]))
            except:
                print('''\ndid: {}\nName: {}\nSalts: {}\nManufacturing Date: {}\nProducer: {}\nPrice: {}\nQuantity: {}\nCategory: {}\n'''.format(lst[0], lst[1], lst[2], lst[3], lst[4],lst[5], lst[6], lst[7]))
        else:
            # Employee
            print('''\neid: {}\nName: {}\nPan Number: {}\nAadhaar Number: {}\nAge: {}\nDob: {}\nDepartment: {}\nEmail: {}\nGender: {}\nPhone: {}\nAddress: {}\n'''.format(lst[0], lst[1], lst[2], lst[3], lst[4], lst[5], lst[6], lst[7], lst[8], lst[9], lst[10]))

    
    def Verify(self, login_ID, login_pswd, opt):
        if(opt == 1):
            query = '''SELECT employee_login_id FROM employee_credentials WHERE employee_login_id = "{}" AND employee_login_password = "{}"'''.format(login_ID, login_pswd)
        else:
            query = '''SELECT consumer_login_id FROM consumer_credentials WHERE consumer_login_id = "{}" AND consumer_login_password = "{}"'''.format(login_ID, login_pswd)
        l = []
        try:
            self.connection.cur.execute(query)

            l += self.connection.cur.fetchall()
            if(len(l) == 1):
                return 1
            return 0
        except:
            print("Invalid Query")

    def My_Acc(self, ID, opt):
        if(opt == 1):
            query = '''SELECT * FROM employee WHERE eid = "{}"'''.format(ID)
        else:
            query = '''SELECT * FROM consumer WHERE cid = "{}"'''.format(ID)
        try:
            self.connection.cur.execute(query)

            l = list(self.connection.cur.fetchall())
            self.pprint(list(l[0]))
        except:
            print("Invalid Query")

    def Shop(self, opt):
        while True:
            print("---------Welcome to Drug Shop---------\n")
            print("1) Search")
            print("2) List all Drugs")
            if(opt == 1):
                print("3) Add or Remove Drug")
                print("4) Back")
            else:
                print("3) Back\n")
            a = int(input("Enter: "))

            if(a == 1):
                inp = int(input("Enter did: "))
                query = '''SELECT * FROM drug WHERE did = {}'''.format(inp)
                try:
                    self.connection.cur.execute(query)
                    l = list(self.connection.cur.fetchall())
                    self.pprint(list(l[0]))
                except:
                    print("No such drug exists or available\n")

            elif(a == 2):
                query = '''SELECT * FROM drug'''
                try:
                    self.connection.cur.execute(query)
                    l = list(self.connection.cur.fetchall())
                    for i in range(len(l)):
                        self.pprint(list(l[i]))
                except:
                    print("Unexpected Error occoured")
            
            elif((a == 3 and opt != 1) or (a == 4 and opt == 1)):
                print()
                break

            elif(a == 3 and opt == 1):
                while True:
                    print("1) Add New Drug")
                    print("2) Remove Drug")
                    print("3) Back")
                    aa = int(input("Enter your choice: "))
                    if(aa == 1):
                        i1 = int(input("Enter did: "))
                        i2 = input("Enter Name: ")
                        i3 = input("Enter Salts (XX-XXX-XXXX): ")
                        i4 = input("Enter Manufacturing Date(YYYY-MM-DD): ")
                        i5 = int(input("Enter Producer(pid): "))
                        i6 = float(input("Enter Price: "))
                        i7 = int(input("Enter Quantity: "))
                        i8 = input("Enter Category: ")
                        try:
                            query = '''INSERT into drug (did, dname, salts, m_date, producer, price, quantity, category) values ({}, '{}', '{}', '{}', {}, {}, {}, '{}')'''.format(i1, i2, i3, i4, i5, i6, i7, i8)
                            self.connection.cur.execute(query)
                            self.connection.con.commit()
                        except:
                            print("Error Could not add new Drug")

                    elif(aa == 2):
                        in1 = int(input("Enter did: "))
                        try:
                            query = '''DELETE FROM drug where did = {}'''.format(in1)
                            self.connection.cur.execute(query)
                            self.connection.con.commit()
                        except:
                            print("Error Could not delete Drug with id {}".format(in1))

                    elif(aa == 3):
                        print()
                        break
                    
                    else:
                        print("Invalid Input Try Agian\n")

            elif((a == 3 and opt != 1) or (a == 4 and opt == 1)):
                print()
                break

            else:
                print("Invalid Input Please try again\n")

    def OLAP(self, inp):
        if(inp == 1):
            try:
                query = '''SELECT sex, age, count(cid)
                        FROM consumer
                        group by sex, age with rollup;'''
                self.connection.cur.execute(query)
                l = list(self.connection.cur.fetchall())
                for i in range(len(l)):
                    print(list(l[i]))
            except:
                print("Error in Query\n")

        elif(inp == 2):
            try:
                query = '''SELECT rtype, defcon, count(doctor_alloted) as "Count"
                        FROM niche_requirements
                        group by rtype, defcon with rollup;'''
                self.connection.cur.execute(query)
                l = list(self.connection.cur.fetchall())
                for i in range(len(l)):
                    print(list(l[i]))
            except:
                print("Error in Query\n")

        elif(inp == 3):
            try:
                query = '''SELECT sex, specialization, qualifications, count(did) as "Count"
                        FROM doctor
                        group by sex, specialization, qualifications with rollup;'''
                self.connection.cur.execute(query)
                l = list(self.connection.cur.fetchall())
                for i in range(len(l)):
                    print(list(l[i]))
            except:
                print("Error in Query\n")

        elif(inp == 4):
            try:
                query = '''SELECT NULL, NULL, qualifications, count(did) as "Count"
                        FROM doctor
                        group by qualifications
                        union all
                        SELECT NULL, specialization, NULL, count(did) as "Count"
                        FROM doctor
                        group by specialization
                        union all
                        SELECT sex, NULL, NULL, count(did) as "Count"
                        FROM doctor
                        group by sex;'''
                self.connection.cur.execute(query)
                l = list(self.connection.cur.fetchall())
                for i in range(len(l)):
                    print(list(l[i]))
            except:
                print("Error in Query\n")

        elif(inp == 5):
            try:
                query = '''SELECT rtype, defcon, count(doctor_alloted) as "Count"
                        FROM niche_requirements
                        group by rtype, defcon with rollup
                        union all
                        SELECT rtype,NULL, count(doctor_alloted) as "Count"
                        FROM niche_requirements
                        group by rtype
                        union all
                        SELECT NULL, defcon, count(doctor_alloted) as "Count"
                        FROM niche_requirements
                        group by defcon
                        union all
                        SELECT NULL, NULL, count(doctor_alloted) as "Count"
                        FROM niche_requirements
                        group by NULL;'''
                self.connection.cur.execute(query)
                l = list(self.connection.cur.fetchall())
                for i in range(len(l)):
                    print(list(l[i]))
            except:
                print("Error in Query\n")

        elif(inp == 6):
            try:
                query = '''SELECT sex, age, count(cid)
                        FROM consumer
                        group by sex, age with rollup
                        union all
                        SELECT NULL, age, count(cid)
                        FROM consumer
                        group by age
                        union all
                        SELECT sex, NULL, count(cid)
                        FROM consumer
                        group by sex
                        union all
                        SELECT NULL, NULL, count(cid)
                        FROM consumer
                        group by NULL;'''
                self.connection.cur.execute(query)
                l = list(self.connection.cur.fetchall())
                for i in range(len(l)):
                    print(list(l[i]))
            except:
                print("Error in Query\n")

    def Triggers(self, inp):
        if(inp == 1):
            try:
                query = '''DROP TRIGGER IF EXISTS `medical_store`.`minimum_sum_insured`'''
                self.connection.cur.execute(query)
                query = "CREATE DEFINER = CURRENT_USER TRIGGER `medical_store`.`minimum_sum_insured` BEFORE INSERT ON `health_insurance` FOR EACH ROW BEGIN IF NEW.sum_insured < 10000 THEN SET NEW.sum_insured = 10000; END IF; END"
                self.connection.cur.execute(query)
                self.connection.con.commit()
                print("Trigger created!\n")
            except:
                print("Error in Query\n")
        
        elif(inp == 2):
            try:
                query = '''DROP TRIGGER IF EXISTS `medical_store`.`minimum_span`'''
                self.connection.cur.execute(query)
                query = "CREATE DEFINER=`root`@`localhost` TRIGGER `minimum_span` BEFORE INSERT ON `health_insurance` FOR EACH ROW BEGIN IF NEW.p_duration < 1 THEN SET NEW.p_duration = 1 AND NEW.p_enddate = NEW.p_startdate + 1; END IF;  END"
                self.connection.cur.execute(query)
                self.connection.con.commit()
                print("Trigger created!\n")
            except:
                print("Error in Query\n")

        elif(inp == 3):
            try:
                query = '''DROP TRIGGER IF EXISTS `medical_store`.`employee_password_length`'''
                self.connection.cur.execute(query)
                query = '''CREATE DEFINER = CURRENT_USER TRIGGER `medical_store`.`employee_password_length` BEFORE INSERT ON `employee_credentials` FOR EACH ROW BEGIN IF LENGTH(NEW.employee_login_password) < 8 THEN signal sqlstate '45000' set message_text = 'Invalid Password length (<8)'; end if; END'''
                self.connection.cur.execute(query)
                self.connection.con.commit()
                print("Trigger created!\n")
            except:
                print("Error in Query\n")

        elif(inp == 4):
            try:
                query = '''DROP TRIGGER IF EXISTS `medical_store`.`consumer_password_length`'''
                self.connection.cur.execute(query)
                query = '''CREATE DEFINER = CURRENT_USER TRIGGER `medical_store`.`consumer_password_length` BEFORE INSERT ON `consumer_credentials` FOR EACH ROW BEGIN IF LENGTH(NEW.consumer_login_password) < 8 THEN signal sqlstate '45000' set message_text = 'Invalid Password length (<8)'; end if; END'''
                self.connection.cur.execute(query)
                self.connection.con.commit()
                print("Trigger created!\n")
            except:
                print("Error in Query\n")

        elif(inp == 5):
            try:
                query = "SHOW TRIGGERS"
                self.connection.cur.execute(query)
                self.connection.con.commit()
                l = list(self.connection.cur.fetchall())
                for i in range(len(l)):
                    print(list(l[i]))
            except:
                print("Error in Query\n")