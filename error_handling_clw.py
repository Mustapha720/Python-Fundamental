val1 = input("Input the first value: ")
val2 = input("Input the second value: ")
try:
    result = int(val1) + int(val2)
    print(result)
except ZeroDivisionError:
    print(f"Can't divide {val1} by {val2}")
except TypeError:
    print(f"An integer can't be divided by a string")