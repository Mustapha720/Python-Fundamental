# def eat():
#     """
#     This function simulates the action of eating.
#     """
#     print("Eating...")
# eat()

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
"""
def mult_table():
    value1 = input("Generate multiplication table from: ")
    value2 = input("Generate multiplication table to: ")
    if value1 < value2 and value1 != 0:
        for i in range(value1, value2 + 1):
            print(f"Multiplication Table {1}")
            for j in numbers:
                print(f"{i} x {j} = {i * j}")
    else:
        print("The first value must be greater than zero and less than the second value.")
mult_table()
"""

"""
Parameterized function
def mult_table(num1, num2):
    if num1 < num2 and num1 != 0:
        for i in range(num1, num2 + 1):
            print(f"Multiplication Table {1}")
            for j in numbers:
                print(f"{i} x {j} = {i * j}")
    else:
        print("The first value must be greater than zero and less than the second value.")
value1 = input("Generate multiplication table from: ")
value2 = input("Generate multiplication table to: ")
mult_table(value1, value2)
"""


pin = []
def register():
    user_name = input("Your Username: ")
    email = input("Input your email: ")
    new_pin = input("Input your pin: ")
    print(f"Welcome {user_name}")
register()

def question():
    print("What is ----")

def option():
    print("1. Take test")
    print("2. Log out")
    option = input("Pick an option: ")
    if option == '1':
        question()
    elif option == '2':
        exit()
    else:
        exit()
option()