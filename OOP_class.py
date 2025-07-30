"""
OOP
How to create a class
What is object?
What is class?
Instance
Attributes(color, age, height, ....)
Initialization
Inheritance
Methods
"""

# class Animal:
#     def sleep(self, name):
#         self.name = name
#         print(f"{name} is sleeping")
#         return self.name

# bull_dog = Animal()
# local_dog = Animal()
# german_shepherd = Animal()
# print(bull_dog.sleep("Bulldog"))


class Employee:
    """
    3 parameters: name, location & salary
    """
    bonus = 0.3
    def __init__(self, name, location, salary):
        self.name = name
        self.location = location
        self.salary = salary

    def staff_detail(self):
        detail = (f"My name is {self.name}. My salary is {self.salary}")
        return detail

    def annual_bonus(self):
        self.salary = self.salary * self.bonus
        return self.salary

emp1 = Employee("Shalom", "Lagos", 10000)
emp2 = Employee("Joshua", "Niger", 5000)
emp3 = Employee("Temi", "Oyo", 2000)

emp1.name = "Shalom"
emp1.location = "Lagos"
emp1.salary = 10000

emp2.name = "Joshua"
emp2.location = "Niger"
emp2.salary = 5000

emp3.name = "Temi"
emp3.location = "Oyo"
emp3.salary = 2000

print("Employee 1 details: ", emp1.staff_detail())
print("Employee 1 bonus: ", emp1.annual_bonus())
print("Employee 2 details: ",emp2.staff_detail())
print("Employee 2 bonus: ",emp2.annual_bonus())
print("Employee 3 details: ",emp3.staff_detail())
print("Employee 3 bonus: ",emp3.annual_bonus())