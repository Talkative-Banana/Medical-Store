from lib.basics import connect_to_db
from lib.users import consumer as cm
from lib.users import employee as emp
from lib.basics import multi_funct as mf

DBMS = connect_to_db.DB()
reg = mf.Multi_Functional(DBMS)

def employee_menu(ID):
    while True:
        print("1) My Account")
        print("2) Shop")
        print("3) OLAP Queries")
        print("4) Triggers")
        print("5) Log out\n")
        a = int(input("Enter: "))
        if(a == 1):
            emp.Employee(ID, reg).My_Acc()
        elif(a == 2):
            emp.Employee(ID, reg).Shop()
        elif(a == 3):
            emp.Employee(ID, reg).HandleOLAP()
        elif(a == 4):
            emp.Employee(ID, reg).Triggers()
        elif(a == 5):
            break
        else:
            print("Invalid Input Please try again\n")

def Pres():
    # Not completed Yet
    return

def Ins():
    # Not completed Yet
    return

def consumer_menu(ID):
    while True:
        print("1) My Account")
        print("2) Shop")
        print("3) Prescription")
        print("4) Health Insurance")
        print("5) Log out\n")
        a = int(input("Enter: "))
        if(a == 1):
            cm.Consumer(ID, reg).My_Acc()
        elif(a == 2):
            cm.Consumer(ID, reg).Shop()
        elif(a == 3):
            Pres()
        elif(a == 4):
            Ins()
        elif(a == 5):
            print("Thanks for using Medical Store\n")
            break
        else:
            print("Invalid Input Please try again\n")


def new_acc():
    while True:
        print("1) Employee")
        print("2) Consumer")
        print("3) Back")
        inp = int(input("Enter: "))
        if(inp == 1):
            eid = int(input("Enter eid: "))
            name = input("Enter name: ")
            pannumber = input("Enter pananumber: ")
            aadhaarnumber = input("Enter aadharnumber: ")
            age = int(input("Enter age: "))
            dob = input("Enter dob(YYYY-MM-DD): ")
            dpm = input("Enter dpm[1: 100]: ")
            email = input("Enter email: ")
            gender = input("Enter gender (Male/Female/Agender): ")
            phone = input("Enter phone: ")
            address = input("Enter address: ")
            emp.Employee(-1, reg).SignUP(eid, name, pannumber, aadhaarnumber, age, dob, dpm, email, gender, phone, address)

        elif(inp == 2):
            cid = int(input("Enter cid: "))
            pannumber = input("Enter pananumber: ")
            name = input("Enter name: ")
            gender = input("Enter gender (M/F/A): ")
            age = int(input("Enter age: "))
            email = input("Enter email: ")
            phone = input("Enter phone: ")
            cm.Consumer(-1, reg).SignUP(cid, pannumber, name, gender, age, email, phone)

        else:
            return

def login_attempt(id):
    login_id = input("ID: ")
    login_pwd = input("Password: ")
    if id == 0:
        if (cm.Consumer(-1, reg).Verify(login_id, login_pwd)):
            return login_id
        return -1
    else:
        if (emp.Employee(-1, reg).Verify(login_id, login_pwd)):
            return login_id
        return -1


print("****************** Welcome to Medical Store - Database ******************")
while True:
        print("To login enter:")
        print("1) Enter as Consumer")
        print("2) Enter as Employee")
        print("3) Sign Up")
        print("4) Exit\n")
        a = int(input("Enter: "))
        if(a == 1):
            temp = login_attempt(0)
            # 45    'r3iuduJ'
            if(temp != -1):
                print("Login Successfull\n")
                consumer_menu(temp)
            else:
                print("Invalid Credentials\n")
            
        elif(a == 2):
            temp = login_attempt(1)
            # 91 1FHVum
            if(temp != -1):
                print("Login Successfull\n")
                employee_menu(temp)
            else:
                print("Invalid Credentials\n")

        elif(a == 3):
            new_acc()
        
        elif(a == 4):
            print("Thanks for using Medical Store\n")
            break
        else:
            print("Invalid Input Please try again\n")
import print, int, input