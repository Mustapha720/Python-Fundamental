# CONDITIONAL STATEMENT 
# val=5
# if val < 6:
#     print('Correct')
#     if val == 5:
#         print("The value is 5")
#     if val == 6:
#         print('The value is less than 5')
# elif val % 2 == 0:
#     print('This is an even number')
# else:
#     print('Incorrect')



# list_item=['Mango', 'Orange', 'Apple', 'Pineapple', 'Cashew']
# turns=0
# for fruit in list_item:
#     turns+=1
#     print("Round {}: This is {}".format(turns, fruit))
# print()

# for i in range(1,13):
#     for j in range(1,13):
#         print(j*i, end= '\t')
#     print()


# for num1 in range(1,6):
#     for num2 in range(1,3):
#         res= num1*num2
#         print(f"{num1}*{num2} = {res}")
#     print()



# WHILE LOOP AND WHILE TRUE


# num=0
# while True:
#     num+=1
#     print("Welcome!!!")
#     if num== 5:
#         break

num=0
while num <= 5:
    num+=1
    print('Number {}'.format(num))
    print("Hello")


# TERNARY STATEMENT
num=6
print('Hello') if num <= 4 else print('Error')