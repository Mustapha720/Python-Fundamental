import time
import random as rd

class ATM:
    def __init__(self):
        self.balance = 1000
        self.pinn = []
        self.register_name = []
        self.register_acc = []
        self.Acc_num = None

    def register1(self):
        name = input("Input your name: ")
        print(f"Welcome, {name}")
        num = rd.randint(0000, 9999)
        self.Acc_num = "20" + str(num)
        self.register_acc.append(self.Acc_num)
        print(f"Your new account number is", self.Acc_num)
        self.register_name.append(name)

    def register(self):
        print("Loading...")
        time.sleep(5)
        pinnn = input("Create your pin: ")
        p = input("Confirm pin: ")
        if pinnn != p:
            print("Incorrect pin")
            exit()
        else:
            print("Registration successful!")
        self.pinn.append(p)

    def confirmation(self):
        acc_numm = input("Your account number: ")
        pIn = input("Enter your pin: ")
        if acc_numm != self.Acc_num:
            print("Incorrect account number")
            exit()
        else:
            print("loading.........")
            time.sleep(3)
        if pIn != self.pinn[0]:
            print("Incorrect pin")
            exit()
        else:
            time.sleep(2)

    def menu(self):
        print("""
            ----ATM MENU----
            1. Check Balance
            2. Deposit Money
            3. Transfer
            4. Withdraw
            5. EXIT
            """)

    def check_balance(self):
        pin = input("Input your pin: ")
        if pin != self.pinn[0]:
            print("Incorrect Pin.")
        else:
            print(f"Your current balance is {self.balance}")

    def deposit_money(self):
        amount = int(input("How much do you want to deposit? "))
        pin = input("Input your pin: ")
        if pin != self.pinn[0]:
            print("Incorrect Pin.")
        else:
            if amount > 500:
                self.balance += amount
                print(f"You have successfully deposited {amount}. Your new balance is {self.balance}")
            else:
                print(f"Amount must be greater than 500")

    def withdraw(self):
        amount = int(input("How much do you want to withdraw: "))
        pin = input("Input your pin: ")
        if pin != self.pinn[0]:
            print("Incorrect Pin.")
        else:
            if amount <= self.balance:
                self.balance -= amount
                print(f"You have successfully withdrawn {amount}. Your new balance is {self.balance}")
            else:
                print("Insufficient funds")

    def transfer(self):
        amount = int(input("How much do you want to transfer: "))
        if amount <= self.balance:
            self.balance -= amount
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
            if pin != self.pinn[0]:
                print("Incorrect Pin.")
            else:
                if len(acc) == 10:
                    print(f"Successful. Your new balance is {self.balance}")
                else:
                    print('Incorrect account number')
        elif choice == "2":
            acc = input("Account number: ")
            pin = input("Input your pin: ")
            if pin != self.pinn[0]:
                print("Incorrect Pin.")
            else:
                if len(acc) == 10:
                    print(f"Successful. Your new balance is {self.balance}")
                else:
                    print('Incorrect account number')
        elif choice == "3":
            acc = input("Account number: ")
            pin = input("Input your pin: ")
            if pin != self.pinn[0]:
                print("Incorrect Pin.")
            else:
                if len(acc) == 10:
                    print(f"Successful. Your new balance is {self.balance}")
                else:
                    print('Incorrect account number')
        else:
            return

    def atm_machine(self):
        while True:
            self.menu()
            choice = input("Please select an option (1-5): ")

            if choice == '1':
                self.check_balance()
            elif choice == '2':
                self.deposit_money()
            elif choice == '3':
                self.transfer()
            elif choice == '4':
                self.withdraw()
            elif choice == '5':
                print("Thank you for using the ATM. Goodbye!")
                break
            else:
                print("Invalid option. Please choose a valid option")

# Run the ATM as before, but now using the class
atm = ATM()
atm.register1()
atm.register()
atm.confirmation()
atm.atm_machine()