import time
import random as rd


class LoanApp():
    def __init__(self):
        self.loan_amount = []
        self.interest = []

    def loan(self):
        amount = int(input("How much do you want to borrow/loan: "))
        self.loan_amount.append(amount)
        self.interest = amount + (amount * 0.10)
        print(f"10% has been added to {amount}")
        print(f"You have successfully borrowed/loaned {self.interest}")

    def loan_repayment(self):
        amount = int(input("How much do you want to pay: "))
        self.interest -= amount
        if self.interest == 0.0:
            print(f"You have successfully repaid your debt!")
        else:
            print(f"You still have {self.interest} to pay")

    def loan_calculator(self):
        amount = int(input("How much: "))
        duration = int(input("Duration: "))
        interest = amount + (amount * 0.10)
        total = interest / duration
        print(f"Total amount with interest(10%) is: {interest} \nYou'll pay {total} for {duration} month")

    def  loan_menu(self):
        print("""
                -------Loan Menu-------
                1. Loan
                2. Loan Repayment
                3. Loan Calculator
                4. Exit
                """)

    def menu_loan(self):
        while True:
            self.loan_menu()
            choice = input("Select an option(1-3): ")
            if choice == '1':
                self.loan()
            elif choice == '2':
                self.loan_repayment()
            elif choice == '3':
                self.loan_calculator()
            elif choice == '4':
                return
            else:
                break

l = LoanApp()



class Bank(LoanApp):
    def __init__(self, name, Acc_num):
        self.name = name
        self.account_number = Acc_num
        self.balance = 1000
        self.pinn = []
        self.register_name = []
        self.register_acc = []

    def register(self):
        global pin
        self.name = input("Input your name: ")
        print(f"Welcome, {self.name}!!!")
        self.register_name.append(self.name)
        num = rd.randint(0000, 9999)
        self.account_number = "20" + str(num)
        self.register_acc.append(self.account_number)
        print(f"Your new account number is", self.account_number)
        pin = input("Create your pin: ")
        if len(pin) == 4:
            self.pinn.append(pin)
            confirm_pin = input("Confirm pin: ")
            if confirm_pin != pin:
                print("Incorrect Pin")
                exit()
            else:
                print("Loading.....")
                time.sleep(4)
                return
        else:
            print("The PIN must be exactly 4 digits long.")
            exit()

    def confirmation(self):
        print("Authenticating.....")
        time.sleep(3)
        acc = input("Your account number: ")
        if acc != self.register_acc[0]:
            print("Incorrect account number")
            return self.confirmation()
        else:
            p = input("Your pin: ")
            if p != self.pinn[0]:
                print("Incorrect Pin")
                exit()
            else:
                print("Loading.....")
                time.sleep(3)
                return
            if acc != self.account_number:
                print("Incorrect")
            else:
                return

    def deposit(self):
        amount = input("How much do you want to deposit: ")
        c_p = input("Input your pin: ")
        if c_p == self.pinn[0]:
            print("Loading.....")
            time.sleep(2)
            amount += self.balance
            print(f"Your new balance is {self.balance}")
        else:
            print("Incorrect pin")
            return

    def check_balance(self):
        c_p = input("Input your pin: ")
        if c_p == self.pinn[0]:
            print(f"Your current balance is {self.balance}")
        else:
            print("Incorrect pin")
            return

    def transfer(self):
        amount =  int(input("How much do you want to transfer: "))
        print("""
                -------Bank-------
                1. Access Bank
                2. UBA
                3. Polaris Bank
                """)
        choi = input("To which bank(1-3)? ")
        if choi == '1':
            no = input("Account number: ")
            if len(no) == 6:
                c_p = input("Input your pin: ")
                if c_p != self.pinn[0]:
                    print("Incorrect Pin")
                else:
                    if amount > self.balance:
                        print("Insufficient funds")
                    else:
                        print("Loading.....")
                        time.sleep(2)
                        self.balance -= amount
                        print(f"Successful transaction! You have transferred {amount} to {no}")
                        print(f"Your current balance is {self.balance}")
            else:
                print("The Account No. must be exactly 6 digits long.")
        elif choi == '2':
            no = input("Account number: ")
            if len(no) == 6:
                c_p = input("Input your pin: ")
                if c_p != self.pinn[0]:
                    print("Incorrect Pin")
                else:
                    if amount > self.balance:
                        print("Insufficient funds")
                    else:
                        print("Loading.....")
                        time.sleep(2)
                        self.balance -= amount
                        print(f"Successful transaction! You have transferred {amount} to {no}")
                        print(f"Your current balance is {self.balance}")
            else:
                print("The Account No. must be exactly 6 digits long.")
        elif choi == '3':
            no = input("Account number: ")
            if len(no) == 6:
                c_p = input("Input your pin: ")
                if c_p != self.pinn[0]:
                    print("Incorrect Pin")
                else:
                    if amount > self.balance:
                        print("Insufficient funds")
                    else:
                        print("Loading.....")
                        time.sleep(2)
                        self.balance -= amount
                        print(f"Successful transaction! You have transferred {amount} to {no}")
                        print(f"Your current balance is {self.balance}")
            else:
                print("The Account No. must be exactly 6 digits long.")
        else:
            print("Option does not exist!")

    def withdraw(self):
        amount = int(input("How much do you want to withdraw: "))
        if amount > self.balance:
            print("Insufficient funds")
        else:
            print("Loading.....")
            time.sleep(2)
            self.balance -= amount
            print(f"Successful transaction!")
            print(f"Your current balance is {self.balance}")

    def menu(self):
        print("""
            -------SELECT------
            1. Check Balance
            2. Deposit
            3. Transfer
            4. Withdraw
            5. Loan
            6. Exit
            """)
    
    def atm_machine(self):
        while True:
            self.menu()
            choice = input("Select an option (1-5): ")
            if choice == '1':
                self.check_balance()
            elif choice == '2':
                self.deposit()
            elif choice == '3':
                self.transfer()
            elif choice == '4':
                self.withdraw()
            elif choice == '5':
                self.menu_loan()
            elif choice == '6':
                print("Thank you for using our bank!! Have a nice day!")
                exit()
            else:
                break
atm = Bank("Default_Name", "1234567")
atm.register()
atm.confirmation()
# atm.menu()
atm.atm_machine()