import time
import random as rd
balance = 1000
pinn = []
register_name = []
register_acc = []

def register1():
    global Acc_num
    name = input("Input your name: ")
    print(f"Welcome, {name}")
    num = rd.randint(0000, 9999)
    Acc_num = "20" + str(num)
    register_acc.append(Acc_num)
    print(f"Your new account number is", Acc_num)
    register_name.append(name)
register1()


def register():
    global pinn
    # global p
    # print("INSERT YOUR CARD")
    print("Loading...")
    time.sleep(5)
    pinnn = input("Create your pin: ")
    p = input("Confirm pin: ")
    if pinnn != p:
        print("Incorrect pin")
        exit()
    else:
        print("Registration successful!")
    # pinn = p
    pinn.append(p)
register()

def confirmation():
    acc_numm = input("Your account number: ")
    pIn = input("Enter your pin: ")
    if acc_numm != Acc_num:
        print("Incorrect account number")
        exit()
    else:
        print("loading.........")
        time.sleep(3)
    if pIn != pinn[0]:
        print("Incorrect pin")
        exit()
    else:
        time.sleep(2)
confirmation()

def menu():
    # print(balance)
    print("""
            ----ATM MENU----
            1. Check Balance
            2. Deposit Money
            3. Transfer
            4. Withdraw
            5. EXIT
            """)


def check_balance():
    pin = input("Input your pin: ")
    if pin != pinn[0]:
        print("Incorrect Pin.")
    else:
        print(f"Your current balance is {balance}")


def deposit_money():
    global balance
    amount = int(input("How much do you want to deposit? "))
    pin = input("Input your pin: ")
    if pin != pinn[0]:
        print("Incorrect Pin.")
    else:
        if amount > 500:
            balance += amount
            print(f"You have successfully deposited {amount}. Your new balance is {balance}")
        else:
            print(f"Amount must be greater than 500")


def withdraw():
    global balance
    amount = int(input("How much do you want to withdraw: "))
    pin = input("Input your pin: ")
    if pin != pinn[0]:
        print("Incorrect Pin.")
    else:
        if amount <= balance:
            balance -= amount
            print(f"You have successfully withdrawn {amount}. Your new balance is {balance}")
        else:
            print("Insufficient funds")

def transfer():
    global balance
    amount = int(input("How much do you want to transfer: "))
    if amount <= balance:
        balance -= amount
    else:
        print("Insufficient funds")
        return
    print("""
                1. Access Bank
                2. UBA Bank
                3. GTB Bank
                """)
    choice = input("Which bank do you want to use: ")
    if choice == "1":
        acc = input("Account number: ")
        pin = input("Input your pin: ")
        if pin != pinn[0]:
            print("Incorrect Pin.")
        else:
            if len(acc) == 10:
                print(f"Successful. Your new balance is {balance}")
            else:
                print('Incorrect account number')
    elif choice == "2":
        acc = input("Account number: ")
        pin = input("Input your pin: ")
        if pin != pinn[0]:
            print("Incorrect Pin.")
        else:
            if len(acc) == 10:
                print(f"Successful. Your new balance is {balance}")
            else:
                print('Incorrect account number')
    elif choice == "3":
        acc = input("Account number: ")
        pin = input("Input your pin: ")
        if pin != pinn[0]:
            print("Incorrect Pin.")
        else:
            if len(acc) == 10:
                print(f"Successful. Your new balance is {balance}")
            else:
                print('Incorrect account number')
    else:
        return

def atm_machine():
    while True:
        menu()
        choice = input("Please select an option (1-5): ")

        if choice == '1':
            check_balance()
        elif choice == '2':
            deposit_money()
        elif choice == '3':
            transfer()
        elif choice == '4':
            withdraw()
        elif choice == '5':
            print("Thank you for using the ATM. Goodbye!")
            break
        else:
            print("Invalid option. Please choose a valid option")
atm_machine()