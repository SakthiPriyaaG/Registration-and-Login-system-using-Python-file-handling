
import re

def userchoose():
  print("Welcome.Kindly enter an option to proceed further")
  option=input("Login|Registration: ")
  if option=="Registration":
    Registration()
  elif option=="Login": 
    Login()
  else:
    print("Kindly enter a valid parameter and try again")
    
def Registration():
  datum=open("DatabaseRL.txt",'r')
  print("Welcome to Registration")  
  
  emailValidation=re.compile(r'[A-Za-z]+@[A-Za-z]+.[A-Z|a-z]+')
  email=input("Email|Username: ")
  if re.match(emailValidation, email):
    print("Username created sucessfully")
  else:
    print("Kindly enter valid Mail ID")
  
  passwordValidation=re.compile(r"^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[!@#$%^&*-?]).{5,16}$")
  password=input("Password: ")
  if re.fullmatch(passwordValidation,password):
    print("Password created sucessfully")
  else:
    print("Strong password is recommended.Please try again")
  
  datum=open("DatabaseRL.txt",'a') 
  datainput=email+','+password  
  data=datum.write(datainput+"\n")
  print("Registration is done successfully")
  print("Login to proceed further")

def Login():
  def forgotpassword():
      db=open("DatabaseRL.txt",'rt')
      d=[]
      f=[]
      for i in db:
        a,b=i.split(",")
        b=b.strip()
        c=a,b
        d.append(a)
        f.append(b)
        data=dict(zip(d,f))
      if user1 in data:
        print(data.get(user1))
        print("Kindly note your password and proceed Login")

  print("Welcome to Login")

  user1=input("Enter email|Username: ")
  passwd1=input("Password: ")

  datainput1=user1+','+passwd1

  myfile = open("DatabaseRL.txt", "rt")
  contents = myfile.read()
  myfile.close()

  if datainput1 in contents:
    print("Login sucessful")
  elif datainput1 not in contents:
    print("Ivaild Email and Password!!!")
    print("Kindly register and proceed for login")

  if user1 in contents and passwd1 not in contents:
    print("Or Forgot Password???")
    choose=input("Enter Y/N: ")
    if choose=="Y":
        forgotpassword()
    elif choose=="N":
        print("Kindly register and proceed to login")
    else:
        print("Entry not valid")
      
    
userchoose()
