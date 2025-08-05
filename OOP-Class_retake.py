# class Bank:
#     name = "Onyx Bank Limited"
#     motto = "Transaction made easy for all...."
#     location = "Ijebu Remo"
# uba = Bank()
# uba.name = "United Banks For Africa"
# uba.motto = "Everything we do, we do it well"
# uba.location = "Lagos"
# fidelity = Bank()
# fidelity.name = "Fidelity Bank"
# fidelity.motto = "Everything we do, we do it well"
# fidelity.location = "Lagos"
# wema = Bank()
# wema.name = "Wema Bank"
# wema.motto = "Everything we do, we do it well"
# wema.location = "Lagos"
# zenith = Bank()
# zenith.name = "Zenith Bank"
# zenith.motto = "Everything we do, we do it well"
# zenith.location = "Lagos"
# First_Bank = Bank()
# First_Bank.name = "First Bank"
# First_Bank.motto = "Everything we do, we do it well"
# First_Bank.location = "Lagos"
# Access = Bank()
# Access.name = "Access Bank"
# Access.motto = "Everything we do, we do it well"
# Access.location = "Lagos"
# print(uba.name)




class Bank():
    balance = 0
    def __init__(self, name, motto, location):
        self.name = name
        self.motto = motto
        self.location = location
    def saving(self):
        user = int(input('Enter your amount: '))
        print(f'Your initial balance is {self.balance}')
        self.balance += user
        print(f'Thank you for saving {user} with {self.name}')
    def check_balance(self):
        return self.balance

uba = Bank(name = "United Bank of Africa", location = "Lagos", motto = "Everything we do, we do it well")
print(f"Name: {uba.name} \nMotto: {uba.motto} \nLocation: {uba.location}")
uba.saving()
print("Your current balance is", uba.check_balance())