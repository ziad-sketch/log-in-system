import json
try:
    with open("accounts.json","r") as file:
        accounts=json.load(file)
except FileNotFoundError:
    accounts={}
while True: 
    
    print("\n1 Add username and password | 2 View username and password  | 3 Search | 4 Exit")
    opt=input("Choose option : ")
    if opt=="1":
        x=input("Enter username: ")
        y=input("Enter password: ")
        if x in accounts:
            print("already inserted")
        elif x.strip()==""or y.strip()=="":
            print("invalid username or password")
        else:

       
            
       
         accounts[x]=y
         with open("accounts.json","w")as file:
               json.dump(accounts,file)
         print("account saved successfuly")
    elif opt=="2":
        if len(accounts)==0:
            print("No accounts found")
        else:
            for username , password in accounts.items():
                print(username,":",password)
    elif opt=="3":
        z=input("Search account")
        if z in accounts:
            print(z,":",accounts[z])
        else:
            print("not found")
    elif opt=="4":
        z=input("log in username")
        x=input("Enter password")
        if z  in accounts and accounts[z]==password:
                print ("log in succesfuly")
                continue
        else:
            print("invalid ")
    else:
        print("invalid option")    

