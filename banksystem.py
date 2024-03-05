
#Banking Application


accountNo = 0
customerName = " "
branchCode = " "
mobileNo = 0
balance = 0
def createAccount():
    global accountNo
    global customerName
    global branchCode
    global mobileNo
    global balance
    
    accountNo = int(input("Enter Account Number: "))
    customerName = input("Enter customer Name: ")
    branchCode = input("Enter branch code: ")
    mobileNo = int(input("Enter your mobile number: "))
    balance = int(input("Enter balance: "))


def showDetails():
    print("Account No: ",accountNo)
    print("CustomerName: ",customerName)
    print("Branch code: ",branchCode)
    print("Mobile number: ",mobileNo)


def deposit(amount):
    if(amount<=0):
        print("The amount deposited should be greater than zero rupees")
    else:
        global balance
        balance = balance + amount
        print("The amount",+amount,"is deposited successfully")
        checkBalance()


def withdraw(amount):
    global balance
    if(balance < amount):
        print("Insufficient Funds")
    else:
       balance = balance - amount
       print("The amount", amount, "is successfully withdrawn")
       checkBalance() 
    

def checkBalance():
    print("Available Bank balance: ",balance)

#....main.....#

ch1 = "yes"
while(ch1 == "yes"):
    print("1). create Account")
    print("2). showDetails")
    print("3). deposit")
    print("4). withdraw")
    print("5). checkBalance")
    print("6). Exit")

    ch = int(input("Select any one option: "))
    if(ch == 1):
        createAccount()

    elif(ch == 2):
        showDetails()

    elif(ch == 3):
        amount = int(input("Enter amount to deposit: "))
        deposit(amount)

    elif(ch == 4):
        amount = int(input("Enter amount to withdraw: "))
        withdraw(amount)
        
    elif(ch == 5):
        checkBalance()

    elif(ch == 6):
        print("Your request of exit is successfull")
        
    else:
        print("Please select any 4 options available above")


    print("Do you want to continue ... press yes")

    ch1 = input()



      

        
    
    
    
