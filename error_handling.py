# Error handling
# Difference between Syntax Error and Exceptions
# TRY and EXCEPT Statement – Catching Exceptions
# Try and except statements are used to catch and handle exceptions in Python. Statements that can raise exceptions are kept inside the try clause and the statements that handle the exception are written inside except clause.

amount = 10000
if(amount > 2999):
    print("You are eligible to purchase the goods")

# Exceptions: Exceptions are raised when the program is syntactically correct, but the code results in an error. This error does not stop the execution of the program, however, it changes the normal flow of the program.

# Types of error
# 1. zeroDivisionError
score = 100
# average = score / 0
# print(average)    #will raise zeroDivisionError 
try:
    average = score / 0
    print(average)
except ZeroDivisionError:
    print("Can't divide number by zero")

# 2. Type error
# x = 5
# y = "6"
# z = x + y
# print(z)

# catching the error
x = 5
y = "6"
try:
    z = x + y
    print(z)
except TypeError:
    print("Error: cannot add an int and a str")


# 3. IndexError

num = [1, 2, 3]
try: 
    print ("Second element = %d" %(num[1]))   #%d is a placeholder to collect  the index (as decimal) coming from num and %(a[1]) is called formatting

    print ("Fourth element = %d" %(num[3]))

except IndexError:
    print ("index out of range")




# def division(val1, val2):
#         res = round(val1 / val2)
#         print(res)


# try:
#     val1 = int(input("Enter value one: "))
#     val2 = int(input("Enter value two: "))
#     # print(type(val1))
    
#     division(val1, val2)
# except ValueError:
#     print("Values must be integers")
# except ZeroDivisionError:
#     print('Divisor cannot be zero')